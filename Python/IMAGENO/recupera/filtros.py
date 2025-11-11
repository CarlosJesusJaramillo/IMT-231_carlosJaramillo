import numpy as np
from scipy.ndimage import gaussian_filter, uniform_filter

def filtro_gaussiano(im, sigma=1):
    return gaussian_filter(im, sigma=sigma)

def filtro_promedio(im, size=3):
    return uniform_filter(im, size=size)

def filtro_unsharp(im, sigma=1, amount=1.0):
    blurred = gaussian_filter(im, sigma=sigma)
    sharpened = im + amount*(im - blurred)
    sharpened = np.clip(sharpened, 0, 255)
    return sharpened.astype(np.uint8)
