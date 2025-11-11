# promp/bordes.py
import numpy as np
import matplotlib.pyplot as plt
import scipy.ndimage as ndi
from .utils import to_float01

def detectar_bordes_y_segmentacion(im, k=0.5, close_iter=2, mostrar=True):
    imf = to_float01(im)
    sobel_x = ndi.sobel(imf, axis=0)
    sobel_y = ndi.sobel(imf, axis=1)
    edges = np.hypot(sobel_x, sobel_y)
    thresh = imf.mean() + k * imf.std()
    mask_final = imf > thresh
    mask_final = ndi.binary_closing(mask_final, iterations=close_iter)
    mask_final = ndi.binary_fill_holes(mask_final)
    objeto = np.where(mask_final, imf, 0)

    if mostrar:
        fig, axes = plt.subplots(1, 4, figsize=(14, 4))
        for ax, img, title in zip(
            axes,
            [imf, edges, mask_final, objeto],
            ["Base", "Bordes", "Máscara", "Objeto"],
        ):
            ax.imshow(img, cmap="gray")
            ax.set_title(title)
            ax.axis("off")
        plt.tight_layout()
        plt.show()

    return edges, mask_final, objeto