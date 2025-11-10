# imagenoop/__init__.py
# ===============================
# ImagenOOP - Inicialización del paquete
# ===============================

# --- Carga de imágenes ---
from .carga import cargar_imagen, listar_imagenes, cargar_volumen, descomprimir_zip

# --- Visualización ---
from .visualizacion import mostrar_imagen, mostrar_subplots, mostrar_cortes_planos

# --- Filtros ---
from .filtros import (
    filtro_mediana,
    filtro_gaussiano,
    filtro_promedio,
    aplicar_filtros_automaticos,
    detectar_bordes_sobel,
    detectar_bordes_kernels
)

# --- Máscaras ---
from .mascaras import aplicar_mascara, aplicar_mascara_interactiva

# --- Mediciones e histogramas por objeto ---
from .mediciones import (
    etiquetar,
    bounding_boxes,
    media_pixeles,
    varianza_pixeles,
    histogramas_pixeles,
    plot_histogramas
)

# --- Histograma global ---
from .histograma import mostrar_histograma_cdf
