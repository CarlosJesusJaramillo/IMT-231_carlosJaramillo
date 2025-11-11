# promp/promp.py
import numpy as np
from scipy.ndimage import label
from promp.carga import cargar_imagen_con_barra
from promp.histogramas import (
    hist_y_cdf,
    plot_hist_y_cdf,
    ecualizar_por_cdf,
    mediciones_por_labels,
)
from promp.mascaras import (
    suavizar_mediana,
    generar_mascara,
    mostrar_mascaras_lado_a_lado,
    etiquetar_y_overlay,
    extraer_objeto_por_indice,
)
from promp.filtros import aplicar_filtros_sobre_imagen
from promp.bordes import detectar_bordes_y_segmentacion
from promp.utils import mostrar_gray

RUTA_IMAGEN = "radiografia1.dcm"  # cambia el nombre de tu archivo aquí

def main():
    im = cargar_imagen_con_barra(RUTA_IMAGEN)

    hist, edges, cdf = hist_y_cdf(im)
    plot_hist_y_cdf(hist, edges, cdf)

    im_eq = ecualizar_por_cdf(im)
    mostrar_gray(im_eq, "Imagen ecualizada")

    im_med = suavizar_mediana(im_eq, size=3)
    mask_ini = generar_mascara(im_med, umbral=60, cerrar=False)
    mask_adj = generar_mascara(im_med, umbral=60, cerrar=True)
    mostrar_mascaras_lado_a_lado(mask_ini, mask_adj)

    labels, nlabels, _ = etiquetar_y_overlay(mask_adj)
    print(f"[main] objetos detectados: {nlabels}")
    mediciones_por_labels(im, labels, indices=[1, 2])

    extraer_objeto_por_indice(im, labels, index=1)

    aplicar_filtros_sobre_imagen(im_eq)
    detectar_bordes_y_segmentacion(im_eq, k=0.5)

    labels_mask, nlabels2 = label(mask_adj)
    if nlabels2 > 0:
        areas = [np.sum(labels_mask == (i + 1)) for i in range(nlabels2)]
        idx_max = int(np.argmax(areas)) + 1
        pixeles_obj = im[labels_mask == idx_max]
        print(
            f"[main] objeto mayor (label {idx_max}): "
            f"media={pixeles_obj.mean():.2f}, var={pixeles_obj.var():.2f}"
        )
    else:
        print("[main] no se encontraron objetos.")

if _name_ == "_main_":
    main()