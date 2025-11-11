import numpy as np
from scipy.ndimage import sobel, laplace
import scipy.ndimage as ndi
import matplotlib.pyplot as plt
from .mascaras import ajustar_mascara, otsu_umbral, umbral_simple

def sobel_magnitud(im):
    dx = sobel(im, axis=0)
    dy = sobel(im, axis=1)
    mag = np.hypot(dx, dy)
    mag = 255 * mag / np.max(mag)
    return mag.astype(np.uint8)

def laplaciano(im):
    lap = laplace(im)
    lap = 255 * (lap - lap.min()) / (lap.max() - lap.min())
    return lap.astype(np.uint8)

def segmentar_y_extraer_objeto(im, metodo_borde='sobel', umbral=None, operacion='closing', size=3, mostrar=True):
    if metodo_borde == 'sobel':
        bordes = sobel_magnitud(im)
    elif metodo_borde == 'laplaciano':
        bordes = laplaciano(im)
    else:
        raise ValueError("Metodo de borde no soportado")

    t = otsu_umbral(bordes) if umbral is None else umbral
    mask = umbral_simple(bordes, t)
    mask_final = ajustar_mascara(mask, operacion=operacion, size=size)

    labels, nlabels = ndi.label(mask_final > 0)
    if nlabels == 0:
        return None, mask_final

    areas = [np.sum(labels==i+1) for i in range(nlabels)]
    idx_max = int(np.argmax(areas)) + 1
    bbox = ndi.find_objects(labels)[idx_max-1]
    im_crop = im[bbox]

    if mostrar:
        fig, axes = plt.subplots(1,3, figsize=(15,5))
        axes[0].imshow(im, cmap='gray'); axes[0].set_title('Imagen original'); axes[0].axis('off')
        axes[1].imshow(mask_final, cmap='gray'); axes[1].set_title('Máscara segmentada'); axes[1].axis('off')
        axes[2].imshow(im_crop, cmap='gray'); axes[2].set_title('Objeto extraído'); axes[2].axis('off')
        plt.tight_layout(); plt.show()

    return im_crop, mask_final
