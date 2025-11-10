
import os
import warnings
import numpy as np

try:
    import pydicom
    _HAS_PYDICOM = True
except Exception:
    _HAS_PYDICOM = False

try:
    import imageio.v2 as imageio
except Exception:
    import imageio

def _normalizar_a_uint8(arr):
    arr = np.asarray(arr, dtype=float)
    mn = np.nanmin(arr)
    mx = np.nanmax(arr)
    if mx == mn:
        return np.zeros_like(arr, dtype=np.uint8)
    scaled = (arr - mn) / (mx - mn) * 255.0
    return np.clip(scaled, 0, 255).astype(np.uint8)

def cargar_imagen_dicom(ruta):
   
    if not os.path.exists(ruta):
        raise FileNotFoundError(f"No se encontró el archivo: {ruta}")
    meta = {}
    if _HAS_PYDICOM:
        try:
            ds = pydicom.dcmread(ruta, force=True)
            for k in ['PatientName','PatientID','StudyDate','Modality','SeriesDescription',
                      'PixelSpacing','SliceThickness','ImagePositionPatient','InstanceNumber',
                      'RescaleIntercept','RescaleSlope']:
                if hasattr(ds, k):
                    meta[k] = getattr(ds, k)
            im = ds.pixel_array.astype(float)
            intercept = float(getattr(ds, 'RescaleIntercept', 0.0))
            slope = float(getattr(ds, 'RescaleSlope', 1.0))
            if slope != 1.0 or intercept != 0.0:
                im = im * slope + intercept
            im8 = _normalizar_a_uint8(im)
            return im8, meta
        except Exception as e:
            warnings.warn(f"pydicom no pudo leer el archivo ({e}); se intentará con imageio.")
    try:
        im = imageio.imread(ruta)
        if im.ndim == 3:
        
            im = np.mean(im[..., :3], axis=2)
        im8 = _normalizar_a_uint8(im)
        return im8, meta
    except Exception as e:
        raise RuntimeError(f"No se pudo cargar la imagen con imageio: {e}")

def cargar_imagen_si_es_posible(ruta):
    return cargar_imagen_dicom(ruta)


# En la imagen proporcionada es capaz de mostrar la imagen y devolvernos como tal el tamaño de esta como la cual es una matriz, otra mas de algunos metadatos
# O informacion extra que se llegue a tener.

