# imagenoop/mediciones.py
import numpy as np
import scipy.ndimage as ndi
import matplotlib.pyplot as plt

def etiquetar(mask):
    """
    Etiqueta objetos en una máscara binaria (0/1 o bool).
    Retorna labels (array) y nlabels (int).
    """
    arr = (mask != 0).astype(np.uint8)
    labels, nlabels = ndi.label(arr)
    return labels, nlabels

def bounding_boxes(labels, valor_objeto):
    """
    Devuelve la lista de slices (bounding boxes) para el objeto especificado.
    """
    mask_obj = np.where(labels == valor_objeto, 1, 0)
    return ndi.find_objects(mask_obj)

def media_pixeles(im, labels=None, index=None):
    """Media de intensidad por etiqueta (index puede ser int o lista)."""
    return ndi.mean(im, labels=labels, index=index)

def varianza_pixeles(im, labels=None, index=None):
    """Varianza de intensidad por etiqueta (index puede ser int o lista)."""
    return ndi.variance(im, labels=labels, index=index)

def histogramas_pixeles(im, min_val=0, max_val=255, bins=256, labels=None, index=None):
    """
    Si labels y index se pasan, devuelve histograma por cada etiqueta en index.
    Index puede ser lista, range(...), etc.
    """
    if labels is not None and index is not None:
        return ndi.histogram(im, min=min_val, max=max_val, bins=bins, labels=labels, index=list(index))
    else:
        return ndi.histogram(im, min=min_val, max=max_val, bins=bins)

def plot_histogramas(obj_hists, etiquetas=None):
    """Dibuja múltiples histogramas (obj_hists: lista/iterable de vectores)."""
    for i, hist in enumerate(obj_hists):
        label = f'Objeto {etiquetas[i]}' if etiquetas is not None else f'Objeto {i+1}'
        plt.plot(hist, label=label)
    plt.legend()
    plt.show()
