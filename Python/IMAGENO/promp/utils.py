# promp/utils.py
import numpy as np
import matplotlib.pyplot as plt

def to_float01(im):
    """Convierte cualquier imagen a float en rango 0..1."""
    im = np.asarray(im, dtype=float)
    lo, hi = im.min(), im.max()
    if hi > lo:
        im = (im - lo) / (hi - lo)
    else:
        im = im - lo
    return im

def mostrar_gray(im, title=None, figsize=(5, 5)):
    """Muestra una imagen en escala de grises sin ejes."""
    plt.figure(figsize=figsize)
    plt.imshow(im, cmap="gray")
    if title:
        plt.title(title)
    plt.axis("off")
    plt.tight_layout()
    plt.show()