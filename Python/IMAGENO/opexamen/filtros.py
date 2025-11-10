
import numpy as np
import scipy.ndimage as ndi

def filtro_gaussiano(im, sigma=1.0):
    out = ndi.gaussian_filter(im.astype(float), sigma=sigma)
    return np.clip(out, 0, 255).astype(np.uint8)

def filtro_promedio(im, size=3):
    kernel = np.ones((size, size), dtype=float) / (size*size)
    out = ndi.convolve(im.astype(float), kernel)
    return np.clip(out, 0, 255).astype(np.uint8)

def filtro_unsharp(im, sigma=1.0, amount=1.0):
    imf = im.astype(float)
    blur = ndi.gaussian_filter(imf, sigma=sigma)
    sharp = imf + amount * (imf - blur)
    return np.clip(sharp, 0, 255).astype(np.uint8)
