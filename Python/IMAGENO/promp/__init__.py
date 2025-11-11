# promp/_init_.py
from .carga import cargar_imagen_con_barra
from .utils import to_float01, mostrar_gray
from .histogramas import (
    hist_y_cdf,
    plot_hist_y_cdf,
    ecualizar_por_cdf,
    mediciones_por_labels,
)
from .mascaras import (
    suavizar_mediana,
    generar_mascara,
    mostrar_mascaras_lado_a_lado,
    etiquetar_y_overlay,
    extraer_objeto_por_indice,
)
from .filtros import (
    aplicar_filtros_suavizado,
    aplicar_filtros_sobre_imagen,
)
from .bordes import detectar_bordes_y_segmentacion

_all_ = [
    "cargar_imagen_con_barra",
    "to_float01",
    "mostrar_gray",
    "hist_y_cdf",
    "plot_hist_y_cdf",
    "ecualizar_por_cdf",
    "mediciones_por_labels",
    "suavizar_mediana",
    "generar_mascara",
    "mostrar_mascaras_lado_a_lado",
    "etiquetar_y_overlay",
    "extraer_objeto_por_indice",
    "aplicar_filtros_suavizado",
    "aplicar_filtros_sobre_imagen",
    "detectar_bordes_y_segmentacion",
]