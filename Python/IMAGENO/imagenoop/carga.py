# imagenoop/carga.py
"""
Funciones de carga para ImagenOOP.
- cargar_imagen: carga DICOM o formatos estándar, convierte a escala de grises cuando aplica.
- listar_imagenes: lista rutas por extensiones.
- cargar_volumen: carga todos los DICOM de una carpeta como volumen 3D y devuelve sampling si es posible.
- descomprimir_zip: utilidad simple para zip -> folder.
"""

import os
import zipfile
import numpy as np
import warnings

try:
    import imageio.v2 as imageio
except Exception:
    import imageio

# Intento de usar pydicom para metadatos (opcional)
try:
    import pydicom
    _HAS_PYDICOM = True
except Exception:
    _HAS_PYDICOM = False


def descomprimir_zip(ruta_zip, carpeta_destino="imagenes_ct"):
    """Descomprime un ZIP en carpeta_destino y devuelve la ruta."""
    with zipfile.ZipFile(ruta_zip, 'r') as zip_ref:
        zip_ref.extractall(carpeta_destino)
    return carpeta_destino


def cargar_imagen(ruta):
    """
    Carga una imagen (DICOM si .dcm / fallback imageio para otros formatos).
    Convierte a escala de grises si es RGB.
    Devuelve numpy array o None si falla.
    """
    ext = os.path.splitext(ruta)[1].lower()
    try:
        if ext == '.dcm' or (ext == '' and _HAS_PYDICOM):
            # Intentar leer con pydicom para controlar metadatos y pixel array
            if _HAS_PYDICOM:
                ds = pydicom.dcmread(ruta, force=True)
                im = ds.pixel_array
                # aplicar rescale si existen
                intercept = float(getattr(ds, 'RescaleIntercept', 0.0))
                slope = float(getattr(ds, 'RescaleSlope', 1.0))
                if slope != 1.0 or intercept != 0.0 or im.dtype != np.uint8:
                    im = im.astype(np.float64) * slope + intercept
                    mn, mx = np.nanmin(im), np.nanmax(im)
                    if mx == mn:
                        im = np.zeros_like(im, dtype=np.uint8)
                    else:
                        im = ((im - mn) / (mx - mn) * 255.0).astype(np.uint8)
                else:
                    im = im.astype(np.uint8)
                # si tiene canales, convertir a gris
                if im.ndim == 3 and im.shape[-1] in (3, 4):
                    im = np.mean(im[..., :3], axis=2).astype(np.uint8)
                return im
            else:
                # fallback imageio
                im = imageio.imread(ruta)
                if im.ndim == 3:
                    im = np.mean(im, axis=2).astype(np.uint8)
                return im
        else:
            # formatos comunes
            im = imageio.imread(ruta)
            if im.ndim == 3:
                im = np.mean(im, axis=2).astype(np.uint8)
            return im
    except Exception as e:
        warnings.warn(f"Error cargando imagen {ruta}: {e}")
        return None


def listar_imagenes(carpeta, extensiones=None):
    """Devuelve lista de rutas de imágenes en la carpeta (ordenadas)."""
    if extensiones is None:
        extensiones = ['.dcm', '.jpg', '.jpeg', '.png', '.tif', '.tiff']
    rutas = []
    for root, _, files in os.walk(carpeta):
        for file in files:
            if any(file.lower().endswith(ext) for ext in extensiones):
                rutas.append(os.path.join(root, file))
    rutas = sorted(rutas)
    return rutas


def _try_get_dicom_order_key(path):
    """Intenta obtener InstanceNumber o ImagePositionPatient.z y PixelSpacing/SliceThickness."""
    if not _HAS_PYDICOM:
        return None, None, None
    try:
        ds = pydicom.dcmread(path, stop_before_pixels=True, force=True)
        inst = getattr(ds, 'InstanceNumber', None)
        slice_thickness = getattr(ds, 'SliceThickness', None)
        pixel_spacing = getattr(ds, 'PixelSpacing', None)
        ipp = getattr(ds, 'ImagePositionPatient', None)
        key = None
        if inst is not None:
            key = int(inst)
        elif ipp is not None:
            key = float(ipp[2])
        return key, slice_thickness, pixel_spacing
    except Exception:
        return None, None, None


def cargar_volumen(carpeta):
    """
    Carga todas las imágenes DICOM de una carpeta como volumen 3D.
    Devuelve (volumen, sampling).
    """
    rutas = listar_imagenes(carpeta, extensiones=['.dcm'])
    if not rutas:
        rutas = listar_imagenes(carpeta)
        if not rutas:
            print(f"No se encontraron imágenes en {carpeta}")
            return None, (1.0, 1.0, 1.0)

    sampling = (1.0, 1.0, 1.0)
    if _HAS_PYDICOM:
        orden_info = []
        for r in rutas:
            key, slice_thickness, pixel_spacing = _try_get_dicom_order_key(r)
            orden_info.append((r, key, slice_thickness, pixel_spacing))
        if any(info[1] is not None for info in orden_info):
            orden_info = sorted(orden_info, key=lambda x: (x[1] is None, x[1]))
            rutas = [x[0] for x in orden_info]
        for _, _, slice_thickness, pixel_spacing in orden_info:
            if pixel_spacing is not None:
                try:
                    ps = [float(x) for x in pixel_spacing]
                    d1 = ps[0]
                    d2 = ps[1] if len(ps) > 1 else ps[0]
                    d0 = float(slice_thickness) if slice_thickness is not None else 1.0
                    sampling = (d0, d1, d2)
                    break
                except Exception:
                    continue

    imgs = []
    for ruta in rutas:
        im = cargar_imagen(ruta)
        if im is None:
            warnings.warn(f"Imagen {ruta} no pudo cargarse y será saltada.")
            continue
        imgs.append(im)
    if not imgs:
        print("No se pudieron cargar imágenes del directorio.")
        return None, (1.0, 1.0, 1.0)

    shapes = [im.shape for im in imgs]
    if not all(sh == shapes[0] for sh in shapes):
        raise ValueError("Se encontraron imágenes con diferentes dimensiones. Asegúrate que todos los cortes tengan el mismo tamaño.")

    volumen = np.stack(imgs, axis=0)
    volumen = np.asarray(volumen)
    print(f"Volumen cargado con {volumen.shape[0]} cortes (shape {volumen.shape})")
    return volumen, sampling
