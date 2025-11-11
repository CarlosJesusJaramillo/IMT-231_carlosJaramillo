import numpy as np
import matplotlib.pyplot as plt

def calcular_histograma(im):
    hist, bins = np.histogram(im.flatten(), bins=256, range=(0,255))
    return hist, bins

def ecualizar_histograma(im):
    hist, bins = calcular_histograma(im)
    cdf = hist.cumsum()
    cdf = (cdf - cdf.min()) * 255 / (cdf.max() - cdf.min())
    im_eq = np.interp(im.flatten(), bins[:-1], cdf).reshape(im.shape).astype(np.uint8)
    return im_eq

def plot_histogram(im, titulo="Histograma"):
    hist, bins = calcular_histograma(im)
    plt.figure(figsize=(8,4))
    plt.bar(bins[:-1], hist, width=1.0, color='gray', edgecolor='black')
    plt.title(titulo, fontsize=14)
    plt.xlabel("Intensidad", fontsize=12)
    plt.ylabel("Frecuencia", fontsize=12)
    plt.xlim([0, 255])
    plt.grid(axis='y', alpha=0.3)
    plt.show()

def plot_histogram_cdf(im, titulo="Histograma y CDF"):
    hist, bins = calcular_histograma(im)
    cdf = hist.cumsum()
    cdf_normalizada = cdf / cdf.max()

    plt.figure(figsize=(8,4))
    plt.bar(bins[:-1], hist, width=1.0, color='lightgray', alpha=0.6, edgecolor='black', label="Histograma")
    plt.plot(bins[:-1], cdf_normalizada * hist.max(), color='red', linewidth=2, label="CDF Normalizada")
    plt.title(titulo, fontsize=14)
    plt.xlabel("Intensidad", fontsize=12)
    plt.ylabel("Frecuencia", fontsize=12)
    plt.xlim([0, 255])
    plt.legend()
    plt.grid(axis='y', alpha=0.3)
    plt.show()
