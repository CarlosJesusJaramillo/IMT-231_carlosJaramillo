# 
import numpy as np
import matplotlib.pyplot as plt

def calcular_histograma(im, bins=256):
    arr = np.asarray(im).ravel()
    hist, edges = np.histogram(arr, bins=bins, range=(0,255))
    cdf = hist.cumsum().astype(float)
    if cdf[-1] > 0:
        cdf = cdf / cdf[-1]
    return hist, cdf, edges

def ecualizar_histograma(im):
    im = np.asarray(im).astype(np.uint8)
    hist, cdf, edges = calcular_histograma(im)
    nonzero = np.nonzero(cdf)[0]
    if len(nonzero) == 0:
        return im, hist, cdf
    cdf_min = cdf[nonzero[0]]
    cdf_u = (cdf - cdf_min) / (1.0 - cdf_min + 1e-12)
    lut = (np.clip(cdf_u, 0, 1) * 255.0).astype(np.uint8)
    im_eq = lut[im]
    return im_eq, hist, cdf

def plot_histogram_cdf(im, bins=256, savepath=None):
    hist, cdf, edges = calcular_histograma(im, bins=bins)
    fig, axes = plt.subplots(2,1, figsize=(8,6), sharex=True)
    axes[0].plot(edges[:-1], hist); axes[0].set_title("Histograma")
    axes[1].plot(edges[:-1], cdf); axes[1].set_title("CDF (acumulada)")
    plt.tight_layout()
    if savepath:
        fig.savefig(savepath, bbox_inches='tight', dpi=150)
    return fig
# El calculo de las intensidades como el histograma permite saber cuantas intensidades hay y la cantidad de pixeles por intensidades tiene, y esta se
# ve nuevamente para cunado hacemos una CDF que parece una version mas aplanada debido 
