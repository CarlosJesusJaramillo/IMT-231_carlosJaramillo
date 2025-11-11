# promp/filtros.py
import numpy as np
import matplotlib.pyplot as plt
import scipy.ndimage as ndi
from .utils import to_float01

def aplicar_filtros_suavizado(im):
    imf = to_float01(im)
    w = np.ones((3, 3)) / 9.0
    im_media = ndi.convolve(imf, w)
    im_mediana = ndi.median_filter(imf, size=5)
    im_gauss = ndi.gaussian_filter(imf, sigma=1.0)
    return im_media, im_mediana, im_gauss

def aplicar_filtros_sobre_imagen(im, mostrar=True):
    imf = to_float01(im)
    im_gauss = ndi.gaussian_filter(imf, sigma=1)
    w = np.ones((3, 3)) / 9.0
    im_prom = ndi.convolve(imf, w)
    im_unsharp = imf + 1.2 * (imf - im_gauss)
    sobel_x = ndi.sobel(imf, axis=0)
    sobel_y = ndi.sobel(imf, axis=1)
    im_sobel = np.hypot(sobel_x, sobel_y)
    im_lap = ndi.laplace(imf)

    if mostrar:
        plt.figure(figsize=(10, 8))
        imgs = [
            (imf, "Original"),
            (im_gauss, "Gauss"),
            (im_prom, "Promedio"),
            (im_unsharp, "Unsharp"),
            (im_sobel, "Sobel"),
            (im_lap, "Laplaciano"),
        ]
        for i, (imx, title) in enumerate(imgs, start=1):
            plt.subplot(2, 3, i)
            plt.imshow(imx, cmap="gray")
            plt.title(title)
            plt.axis("off")
        plt.tight_layout()
        plt.show()

    return im_gauss, im_prom, im_unsharp, im_sobel, im_lap