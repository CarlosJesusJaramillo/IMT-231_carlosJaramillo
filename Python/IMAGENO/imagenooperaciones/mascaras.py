import numpy as np

def segmentar_hueso_piel(im_ecualizada):
    """
    Segmenta piel y hueso a partir de una imagen ecualizada.
    """
    mask_skin = (im_ecualizada >= 50) & (im_ecualizada < 179)
    mask_bone = im_ecualizada >= 179
    return mask_skin, mask_bone

def aplicar_mascara(im, mask):
    """
    Aplica una máscara sobre la imagen, dejando 0 donde la máscara es False.
    """
    im_masked = im.copy()
    im_masked[~mask] = 0
    return im_masked
