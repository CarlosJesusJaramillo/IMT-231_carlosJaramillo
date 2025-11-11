import numpy as np
import scipy.ndimage as ndi

def _to_float_norm(im):
    im = np.array(im, dtype=float)
    lo, hi = im.min(), im.max()
    if hi > lo:
        return (im - lo) / (hi - lo)
    return im - lo

def aplicar_filtros_suavizado(im):
    imf = _to_float_norm(im)
    weights = np.ones((3,3)) / 9.0
    im_media = ndi.convolve(imf, weights)
    im_mediana = ndi.median_filter(imf, size=5)
    im_gauss = ndi.gaussian_filter(imf, sigma=1.0)
    return im_media, im_mediana, im_gauss

def aplicar_filtros_sobre_imagen(im):
    imf = _to_float_norm(im)

    im_gauss = ndi.gaussian_filter(imf, sigma=1)
    weights = np.ones((3,3)) / 9.0
    im_prom = ndi.convolve(imf, weights)
    im_unsharp = imf + 1.2 * (imf - im_gauss)
    sobel_x = ndi.sobel(imf, axis=0)
    sobel_y = ndi.sobel(imf, axis=1)
    im_sobel = np.hypot(sobel_x, sobel_y)
    im_lap = ndi.laplace(imf)

    return im_gauss, im_prom, im_unsharp, im_sobel, im_lap


#Entre los filtros que se utilizaron el mejor seria el promedio debido a que realza mejor las estructuras internas, otro pordria ser 
# el sharpening y el que no sale tan bien es el uso del gausiano debido a que este suaviza mucho y quiza el sigma esta muy alto y por esa 
#razon se ve muy difuminado y no se veria tan bien lo que es la imagen.