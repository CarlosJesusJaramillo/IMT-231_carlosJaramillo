

import numpy as np
import scipy.ndimage as ndi

def sobel_magnitud(im):
    imf = im.astype(float)
    sx = ndi.sobel(imf, axis=0)
    sy = ndi.sobel(imf, axis=1)
    mag = np.sqrt(sx**2 + sy**2)
    if mag.max() > 0:
        magn = (mag / mag.max() * 255.0).astype(np.uint8)
    else:
        magn = mag.astype(np.uint8)
    return magn

def laplaciano(im):
    kernel = np.array([[0,1,0],[1,-4,1],[0,1,0]], dtype=float)
    out = ndi.convolve(im.astype(float), kernel)
    mn = out.min(); mx = out.max()
    if mx == mn:
        return np.zeros_like(out, dtype=np.uint8)
    norm = (out - mn) / (mx - mn) * 255.0
    return np.clip(norm, 0, 255).astype(np.uint8)
