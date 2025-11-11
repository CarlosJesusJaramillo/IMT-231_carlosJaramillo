import numpy as np
import matplotlib.pyplot as plt
import scipy.ndimage as ndi

def suavizar_mediana(im, size=3):
    return ndi.median_filter(im, size=size)

def crear_mascara_umbral(im_filt, umbral=60):
    # el valor original era 60 del umbral utilizado para mostrar lo que seria el tejido del hueso
    return (im_filt > umbral)

def cerrar_mascara(mask_start, iterations=1):
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

#En la imagen se pudo observar que moviendo el umbral de nuestra mascara se hace mas presente lo que seria los tejidos internos, como huesos
# en el uso de un umbral <= 60 se observo que se observan mas los tejidos blandos y los bordes de la mano, mientras lo que seria en lo que es 
# un umbral mas alto >= 160 representaria lo que es una imagen relacionada al tejido interno de la mano.
#aunque esta no es de forma perfecta debido a que esta presenta bordes debiles del tejido que esta a su alrededor.