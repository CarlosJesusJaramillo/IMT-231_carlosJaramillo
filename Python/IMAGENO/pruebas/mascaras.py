# pruebas/mascaras.py
import numpy as np
import matplotlib.pyplot as plt
import scipy.ndimage as ndi

def suavizar_mediana(im, size=3):
    return ndi.median_filter(im, size=size)

def crear_mascara_umbral(im_filt, umbral=60):
    # devolver máscara booleana
    return (im_filt > umbral)

def cerrar_mascara(mask_start, iterations=1):
    # esperar booleano de entrada
    mask_bool = mask_start.astype(bool)
    return ndi.binary_closing(mask_bool, iterations=iterations)

def mostrar_mascaras_lado_a_lado(mask_original, mask_ajustada):
    fig, axes = plt.subplots(1, 2, figsize=(8, 4))
    axes[0].imshow(mask_original, cmap='gray', vmin=0, vmax=1)
    axes[0].set_title("Máscara original")
    axes[0].axis('off')

    axes[1].imshow(mask_ajustada, cmap='gray', vmin=0, vmax=1)
    axes[1].set_title("Máscara ajustada")
    axes[1].axis('off')

    plt.tight_layout()
    plt.show()

def etiquetar_y_overlay(mask):
    labels, nlabels = ndi.label(mask)
    # crear overlay usando masked array para que el fondo sea transparente/negro
    overlay = np.ma.masked_where(labels == 0, labels)

    plt.figure(figsize=(6,6))
    plt.imshow(overlay, cmap="nipy_spectral")
    plt.title(f"Regiones etiquetadas (n={nlabels})")
    plt.axis("off")
    plt.tight_layout()
    plt.show()
    return labels, nlabels, overlay

def extraer_objeto_por_indice(im, labels, index=1):
    mask_obj = (labels == index)
    bboxes = ndi.find_objects(labels == index)

    if not bboxes or bboxes[0] is None:
        print(f"No se encontró el objeto con etiqueta {index}")
        return None

    im_crop = im[bboxes[0]]
    plt.figure(figsize=(4,4))
    plt.imshow(im_crop, cmap="gray")
    plt.title(f"Objeto recortado (label {index})")
    plt.axis("off")
    plt.tight_layout()
    plt.show()
    return im_crop
