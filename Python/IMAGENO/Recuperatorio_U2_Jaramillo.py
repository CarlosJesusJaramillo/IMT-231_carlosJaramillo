import os
import numpy as np
import matplotlib.pyplot as plt
from scipy.ndimage import label

from pruebas.carga import cargar_imagen_con_barra
from pruebas.histogramas import mostrar_hist_y_cdf, ecualizar_por_cdf, mediciones_por_labels
from pruebas.mascaras import (
    suavizar_mediana,
    crear_mascara_umbral,
    cerrar_mascara,
    mostrar_mascaras_lado_a_lado,
    etiquetar_y_overlay,
    extraer_objeto_por_indice,
)
from pruebas.filtros import aplicar_filtros_sobre_imagen
from pruebas.bordes import detectar_bordes_y_segmentacion

OUTDIR = os.path.join("pruebas", "output")
os.makedirs(OUTDIR, exist_ok=True)

RUTA_IMAGEN = "imagenRECU.png"

def mostrar_imagen(im, titulo="Imagen"):
    plt.figure(figsize=(5,5))
    plt.imshow(im, cmap='gray')
    plt.title(titulo)
    plt.axis('off')
    plt.tight_layout()
    plt.show()

def main():
    im = cargar_imagen_con_barra(RUTA_IMAGEN) 
    print("Forma:", im.shape)
    print("Tipo de dato:", im.dtype)
    mostrar_imagen(im, "Imagen original")

    hist, cdf = mostrar_hist_y_cdf(im)
    im_eq = ecualizar_por_cdf(im, cdf)
    mostrar_imagen(im_eq, "Imagen ecualizada")

    
    im_med = suavizar_mediana(im, size=3)
    mask_ini = crear_mascara_umbral(im_med, umbral=160)   #<- aqui cambiar el umbral, antes era 60, se cambio para ver tejido interno
    mask_adj = cerrar_mascara(mask_ini, iterations=1)
    mostrar_mascaras_lado_a_lado(mask_ini, mask_adj)
    labels, nlabels, overlay = etiquetar_y_overlay(mask_adj)
    print("Número de objetos etiquetados:", nlabels)

    mediciones_por_labels(im, labels, indices=[1, 5])
    _ = extraer_objeto_por_indice(im, labels, index=1)

    
    im_gauss, im_prom, im_unsharp, im_sobel, im_lap = aplicar_filtros_sobre_imagen(im_eq)

    plt.figure(figsize=(10,8))
    plt.subplot(2,3,1); plt.imshow(im_eq, cmap='gray'); plt.title("Ecualizada"); plt.axis('off')
    plt.subplot(2,3,2); plt.imshow(im_gauss, cmap='gray'); plt.title("Gaussiano"); plt.axis('off')
    plt.subplot(2,3,3); plt.imshow(im_prom, cmap='gray'); plt.title("Promedio"); plt.axis('off')
    plt.subplot(2,3,4); plt.imshow(im_unsharp, cmap='gray'); plt.title("Unsharp"); plt.axis('off')
    plt.subplot(2,3,5); plt.imshow(im_sobel, cmap='gray'); plt.title("Sobel"); plt.axis('off')
    plt.subplot(2,3,6); plt.imshow(im_lap, cmap='gray'); plt.title("Laplaciano"); plt.axis('off')
    plt.tight_layout()
    plt.show()

    edges, mask_final, objeto = detectar_bordes_y_segmentacion(im_eq)

    labels_mask, nlabels2 = label(mask_adj)
    if nlabels2 > 0:
        areas = [np.sum(labels_mask == (i+1)) for i in range(nlabels2)]
        idx_max = int(np.argmax(areas)) + 1
        pixeles_obj = im[labels_mask == idx_max]
        mean_obj = pixeles_obj.mean()
        var_obj = pixeles_obj.var()
        print(f"Objeto mayor (label {idx_max}): media={mean_obj:.2f}, varianza={var_obj:.2f}")
    else:
        print("No se encontraron objetos para medir.")

if __name__ == "__main__":
    main()