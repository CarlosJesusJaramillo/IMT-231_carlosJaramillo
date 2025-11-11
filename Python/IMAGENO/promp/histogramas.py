# promp/histogramas.py
import numpy as np
import matplotlib.pyplot as plt
import scipy.ndimage as ndi
from .utils import to_float01

def hist_y_cdf(im, bins=256):
    im_flat = np.asarray(im).ravel()
    lo, hi = im_flat.min(), im_flat.max()
    hist, edges = np.histogram(im_flat, bins=bins, range=(lo, hi))
    cdf = hist.cumsum().astype(float)
    cdf /= cdf[-1]
    return hist, edges, cdf

def plot_hist_y_cdf(hist, edges, cdf):
    fig, axes = plt.subplots(2, 1, sharex=True, figsize=(6, 6))
    axes[0].plot(edges[:-1], hist, label="Histograma")
    axes[0].legend(loc="upper right")
    axes[1].plot(edges[:-1], cdf, label="CDF")
    axes[1].legend(loc="upper right")
    plt.tight_layout()
    plt.show()

def ecualizar_por_cdf(im, bins=256):
    im = np.asarray(im)
    lo, hi = im.min(), im.max()
    if hi == lo:
        return im.astype(np.uint8)
    hist, edges, cdf = hist_y_cdf(im, bins=bins)
    im_norm = (im - lo) / (hi - lo)
    idx = (im_norm * (bins - 1)).astype(int)
    im_eq = (cdf[idx] * 255).astype(np.uint8)

    fig, axes = plt.subplots(1, 2, figsize=(8, 4))
    axes[0].imshow(im, cmap="gray"); axes[0].set_title("Original"); axes[0].axis("off")
    axes[1].imshow(im_eq, cmap="gray"); axes[1].set_title("Ecualizada"); axes[1].axis("off")
    plt.tight_layout()
    plt.show()

    return im_eq

def mediciones_por_labels(im, labels, indices=None):
    im = np.asarray(im)
    mean_total = ndi.mean(im)
    var_total = ndi.variance(im)
    print(f"[mediciones] media total: {mean_total:.3f}")
    print(f"[mediciones] var total:   {var_total:.3f}")

    try:
        mean_labels = ndi.mean(im, labels=labels)
        print("[mediciones] media por label:", mean_labels)
    except Exception as e:
        print("[mediciones] error en media:", e)

    if indices:
        try:
            mean_sel = ndi.mean(im, labels=labels, index=indices)
            var_sel = ndi.variance(im, labels=labels, index=indices)
            print(f"[mediciones] media {indices}:", mean_sel)
            print(f"[mediciones] var {indices}:", var_sel)
        except Exception as e:
            print("[mediciones] error en indices:", e)