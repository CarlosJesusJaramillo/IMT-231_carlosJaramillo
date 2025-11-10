# imagenoop/filtros.py
"""
Filtros de imagen y detección de bordes para ImagenOOP (mejorado).
Cada salida en aplicar_filtros_automaticos tiene una clave descriptiva
con el nombre del filtro y los parámetros aplicados.
"""
import numpy as np
import scipy.ndimage as ndi

# -------------------------
# Helpers
# -------------------------
def _to_uint8_for_display(arr):
    """
    Convierte/normaliza un array numérico para mostrarlo (0-255 uint8).
    - Si ya es uint8, lo devuelve tal cual.
    - Si es float o entero con rango distinto, lo escala a 0..255.
    """
    a = np.asarray(arr)
    if a.dtype == np.uint8:
        return a
    a_float = a.astype(np.float64)
    mn = np.nanmin(a_float)
    mx = np.nanmax(a_float)
    if mx == mn:
        return np.zeros_like(a_float, dtype=np.uint8)
    norm = (a_float - mn) / (mx - mn)
    return (norm * 255.0).astype(np.uint8)

# -------------------------
# Filtros básicos
# -------------------------
def filtro_mediana(im, size=3):
    """Filtro de mediana. im: array 2D"""
    return ndi.median_filter(im, size=size)

def filtro_promedio(im, size=3):
    """Filtro de media (convolución uniforme)."""
    weights = np.ones((size, size), dtype=float) / (size * size)
    return ndi.convolve(im.astype(float), weights)

def filtro_gaussiano(im, sigma=1):
    """Filtro gaussiano (suavizado)."""
    return ndi.gaussian_filter(im, sigma=sigma)

# -------------------------
# Detección de bordes
# -------------------------
def detectar_bordes_kernels(im, Kx=None, Ky=None):
    """
    Detecta bordes usando kernels personalizados Kx (horizontal) y Ky (vertical).
    Devuelve (Ix, Iy, magnitude).
    """
    imf = im.astype(float)
    if Kx is None:
        Kx = np.array([[-1, -1, -1],
                       [ 0,  0,  0],
                       [ 1,  1,  1]], dtype=float)
    if Ky is None:
        Ky = np.array([[-1, 0, 1],
                       [-1, 0, 1],
                       [-1, 0, 1]], dtype=float)
    Ix = ndi.convolve(imf, Kx)
    Iy = ndi.convolve(imf, Ky)
    mag = np.sqrt(Ix**2 + Iy**2)
    return Ix, Iy, mag

def detectar_bordes_sobel(im):
    """Detecta bordes usando filtro Sobel de SciPy. Retorna (sx, sy, magnitude)."""
    imf = im.astype(float)
    sx = ndi.sobel(imf, axis=0)
    sy = ndi.sobel(imf, axis=1)
    mag = np.sqrt(sx**2 + sy**2)
    return sx, sy, mag

# -------------------------
# Función principal
# -------------------------
def aplicar_filtros_automaticos(im, mediana_size=3, gauss_sigma=1, promedio_size=3, normalize_for_display=True):
    """
    Aplica un conjunto de filtros y detectores de bordes.
    Retorna un diccionario {nombre_descriptivo: imagen_resultado}.
    """
    out = {}
    im_arr = np.asarray(im)

    # original (aseguramos tipo)
    out[f'original ({im_arr.dtype})'] = _to_uint8_for_display(im_arr) if normalize_for_display else im_arr

    # mediana
    try:
        im_med = filtro_mediana(im_arr, size=mediana_size)
        key = f"mediana_size={mediana_size}"
        out[key] = _to_uint8_for_display(im_med) if normalize_for_display else im_med
    except Exception as e:
        out[f"mediana_error"] = f"Error: {e}"

    # gauss
    try:
        im_g = filtro_gaussiano(im_arr, sigma=gauss_sigma)
        key = f"gauss_sigma={gauss_sigma}"
        out[key] = _to_uint8_for_display(im_g) if normalize_for_display else im_g
    except Exception as e:
        out[f"gauss_error"] = f"Error: {e}"

    # promedio
    try:
        im_p = filtro_promedio(im_arr, size=promedio_size)
        key = f"promedio_size={promedio_size}"
        out[key] = _to_uint8_for_display(im_p) if normalize_for_display else im_p
    except Exception as e:
        out[f"promedio_error"] = f"Error: {e}"

    # Sobel
    try:
        sx, sy, smag = detectar_bordes_sobel(im_arr)
        out[f"sobel_ax0 (raw)"] = _to_uint8_for_display(sx) if normalize_for_display else sx
        out[f"sobel_ax1 (raw)"] = _to_uint8_for_display(sy) if normalize_for_display else sy
        out[f"sobel_magnitude (norm)"] = _to_uint8_for_display(smag) if normalize_for_display else smag
    except Exception as e:
        out["sobel_error"] = f"Error: {e}"

    # Kernels personalizados
    try:
        Kx = np.array([[-1, -1, -1],
                       [ 0,  0,  0],
                       [ 1,  1,  1]], dtype=float)
        Ky = np.array([[-1, 0, 1],
                       [-1, 0, 1],
                       [-1, 0, 1]], dtype=float)
        Ix, Iy, mag = detectar_bordes_kernels(im_arr, Kx=Kx, Ky=Ky)
        out[f"Ix_custom (Kx)"] = _to_uint8_for_display(Ix) if normalize_for_display else Ix
        out[f"Iy_custom (Ky)"] = _to_uint8_for_display(Iy) if normalize_for_display else Iy
        out[f"bordes_custom_magnitude (norm)"] = _to_uint8_for_display(mag) if normalize_for_display else mag
    except Exception as e:
        out["kernels_error"] = f"Error: {e}"

    return out


# -------------------------
# Ejecución directa de prueba (opcional)
# -------------------------
if __name__ == "__main__":
    import imageio.v2 as imageio
    import matplotlib.pyplot as plt

    im = imageio.imread("imagenes/hand1.jpg")
    if im.ndim == 3:
        im = np.mean(im, axis=2)
    dic = aplicar_filtros_automaticos(im)
    keys = list(dic.keys())
    vals = [dic[k] for k in keys]
    fig, axes = plt.subplots(1, min(4, len(vals)), figsize=(12,4))
    for i, ax in enumerate(axes):
        ax.imshow(vals[i], cmap='gray')
        ax.set_title(keys[i])
        ax.axis('off')
    plt.show()
        