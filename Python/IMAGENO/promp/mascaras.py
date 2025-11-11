# promp/mascaras.py
import numpy as np
import matplotlib.pyplot as plt
import scipy.ndimage as ndi
from .utils import mostrar_gray

def suavizar_mediana(im, size=3):
    return ndi.median_filter(im, size=size)

def generar_mascara(im, umbral=60, cerrar=True, iterations=1):
    mask = np.asarray(im) > umbral
    if cerrar:
        mask = ndi.binary_closing(mask, iterations=iterations)
    return mask

def mostrar_mascaras_lado_a_lado(mask1, mask2, titles=("Inicial", "Cerrada")):
    fig, axes = plt.subplots(1, 2, figsize=(8, 4))
    for ax, mask, t in zip(axes, [mask1, mask2], titles):
        ax.imshow(mask, cmap="gray", vmin=0, vmax=1)
        ax.set_title(t)
        ax.axis("off")
    plt.tight_layout()
    plt.show()

def etiquetar_y_overlay(mask):
    labels, nlabels = ndi.label(mask)
    overlay = np.ma.masked_where(labels == 0, labels)
    plt.figure(figsize=(6, 6))
    plt.imshow(overlay, cmap="nipy_spectral")
    plt.title(f"Regiones etiquetadas (n={nlabels})")
    plt.axis("off")
    plt.tight_layout()
    plt.show()
    return labels, nlabels, overlay

def extraer_objeto_por_indice(im, labels, index=1):
    slc = ndi.find_objects(labels == index)
    if not slc or slc[0] is None:
        print(f"[extraer] no se encontró etiqueta {index}")
        return None
    obj = im[slc[0]]
    mostrar_gray(obj, f"Objeto recortado (label {index})")
    return obj