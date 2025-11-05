import numpy as np
import matplotlib.pyplot as plt
from scipy import ndimage as ndi

def calcular_histograma(im):
    """Calcula el histograma de la imagen."""
    return ndi.histogram(im, min=0, max=255, bins=256)

def calcular_cdf(hist):
    """Calcula la función de distribución acumulativa (CDF)."""
    return hist.cumsum() / hist.sum()

def mostrar_histograma_cdf(hist, cdf):
    """Muestra histograma y CDF en dos gráficas."""
    fig, axes = plt.subplots(2, 1, sharex=True)
    axes[0].plot(hist, label='Histograma')
    axes[1].plot(cdf, label='CDF')
    for ax in fig.axes:
        ax.legend(loc='center right')
    plt.show()

def ecualizar_imagen(im, cdf):
    """Ecualiza la imagen usando CDF."""
    return (cdf[im] * 255).astype(np.uint8)
