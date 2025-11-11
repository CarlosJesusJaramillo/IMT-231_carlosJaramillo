# pruebas/histogramas.py
import numpy as np
import matplotlib.pyplot as plt
import scipy.ndimage as ndi

def mostrar_hist_y_cdf(im):
    # usar np.histogram para mayor control
    im_flat = np.array(im).ravel()
    hist, bins = np.histogram(im_flat, bins=256, range=(im_flat.min(), im_flat.max()))
    cdf = hist.cumsum().astype(float) / hist.sum()

    fig, axes = plt.subplots(2, 1, sharex=True, figsize=(6,6))
    axes[0].plot(bins[:-1], hist, label="Histograma")
    axes[0].legend(loc="upper right")
    axes[1].plot(bins[:-1], cdf, label="CDF")
    axes[1].legend(loc="upper right")
    plt.tight_layout()
    plt.show()
    return hist, cdf

def ecualizar_por_cdf(im, cdf):
    # si la imagen no está en 0..255, remapear con índices
    im_flat = np.array(im)
    # mapear a 0..255 por posición en bins (simple)
    lo, hi = im_flat.min(), im_flat.max()
    if hi == lo:
        return im_flat
    norm = (im_flat - lo) / (hi - lo)
    indices = (norm * (len(cdf)-1)).astype(int)
    im_eq = (cdf[indices] * 255).astype(np.uint8)

    fig, axes = plt.subplots(1, 2, figsize=(8, 4))
    axes[0].imshow(im_flat, cmap="gray"); axes[0].set_title("Original"); axes[0].axis("off")
    axes[1].imshow(im_eq, cmap="gray"); axes[1].set_title("Ecualizada"); axes[1].axis("off")
    plt.tight_layout()
    plt.show()
    return im_eq

def mediciones_por_labels(im, labels, indices=[1, 5]):
    # usar funciones de scipy.ndimage
    mean_total = ndi.mean(im)
    print("Media total:", mean_total)
    try:
        mean_labels = ndi.mean(im, labels=labels)
        print("Media por label (vector):", mean_labels)
        mean_sel = ndi.mean(im, labels=labels, index=indices)
        print(f"Media etiquetas {indices}:", mean_sel)
    except Exception as e:
        print("Aviso: no se pudieron calcular medias por etiqueta:", e)

    var_total = ndi.variance(im)
    print("Varianza total:", var_total)
    try:
        var_sel = ndi.variance(im, labels=labels, index=indices)
        print(f"Varianza etiquetas {indices}:", var_sel)
    except Exception as e:
        print("Aviso: no se pudieron calcular varianzas por etiqueta:", e)
