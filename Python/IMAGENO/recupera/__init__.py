from .carga import cargar_imagen_dicom
from .histogramas import calcular_histograma, ecualizar_histograma, plot_histogram, plot_histogram_cdf
from .mascaras import otsu_umbral,umbral_simple, ajustar_mascara
from .filtros import filtro_gaussiano, filtro_promedio, filtro_unsharp
from .bordes import sobel_magnitud, laplaciano,segmentar_y_extraer_objeto


