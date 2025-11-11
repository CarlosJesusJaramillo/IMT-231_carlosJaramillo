import imageio.v2 as imageio
import matplotlib.pyplot as plt
import numpy as np

def cargar_imagen_con_barra(ruta, vmin=None, vmax=None, tick_interval=50):
    """
    Carga una imagen (DICOM o raster), la muestra con barra de color y devuelve un ndarray.
    """
    im = imageio.imread(ruta)
    im = np.asarray(im)
    print(f"[carga] dtype: {im.dtype}  shape: {im.shape}")

    if vmin is None:
        vmin = float(im.min())
    if vmax is None:
        vmax = float(im.max())

    plt.figure(figsize=(6, 6))
    plt.imshow(im, cmap="gray", vmin=vmin, vmax=vmax)
    cbar = plt.colorbar()
    tick_vals = np.arange(vmin, vmax + max(1, tick_interval), tick_interval)
    cbar.set_ticks(tick_vals)
    plt.title("Imagen cargada")
    plt.axis("off")
    plt.tight_layout()
    plt.show()

    return im