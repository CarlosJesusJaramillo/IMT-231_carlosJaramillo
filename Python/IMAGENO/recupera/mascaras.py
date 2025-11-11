import numpy as np
from scipy.ndimage import binary_closing, binary_dilation

def umbral_simple(im, umbral):
    mask = (im >= umbral).astype(np.uint8)
    return mask * 255

def otsu_umbral(im):
    hist, _ = np.histogram(im.flatten(), bins=256, range=(0, 255))
    total = im.size
    current_max, threshold = 0, 0
    sum_total = np.dot(np.arange(256), hist)
    sumB, wB = 0, 0
    for i in range(256):
        wB += hist[i]
        if wB == 0:
            continue
        wF = total - wB
        if wF == 0:
            break
        sumB += i * hist[i]
        mB = sumB / wB
        mF = (sum_total - sumB) / wF
        var_between = wB * wF * (mB - mF) ** 2
        if var_between > current_max:
            current_max = var_between
            threshold = i
    return threshold

def ajustar_mascara(mask, operacion='closing', size=3):
    mask_bool = mask > 0
    if operacion == 'closing':
        result = binary_closing(mask_bool, structure=np.ones((size, size)))
    elif operacion == 'dilation':
        result = binary_dilation(mask_bool, structure=np.ones((size, size)))
    else:
        result = mask_bool
    return result.astype(np.uint8) * 255

def aplicar_mascara(im, mask):
    if mask.max() > 1:
        mask_bool = mask > 0
    else:
        mask_bool = mask.astype(bool)
    result = np.zeros_like(im)
    if im.ndim == 2:
        result[mask_bool] = im[mask_bool]
    elif im.ndim == 3:
        result[mask_bool] = im[mask_bool]
    return result
