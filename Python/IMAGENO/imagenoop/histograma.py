# imagenoop/histograma.py
import numpy as np
import matplotlib.pyplot as plt
import scipy.ndimage as ndi

def mostrar_histograma_cdf(im, bins=256):
    """
    Muestra el histograma y la función de distribución acumulativa (CDF) de una imagen.
    """
    im = np.array(im)
    # histogram using ndi (handles any dtype)
    hist = ndi.histogram(im, min=0, max=255, bins=bins)
    cdf = hist.cumsum() / hist.sum()

    fig, axes = plt.subplots(2, 1, figsize=(8, 6), sharex=True)
    axes[0].plot(hist)
    axes[0].set_ylabel("Número de píxeles")
    axes[0].set_title("Histograma")
    axes[1].plot(cdf)
    axes[1].set_xlabel("Intensidad")
    axes[1].set_ylabel("Proporción acumulada")
    axes[1].set_title("CDF (Distribución acumulada)")
    plt.tight_layout()
    plt.show()
