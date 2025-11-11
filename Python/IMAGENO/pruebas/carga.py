# pruebas/carga.py
import imageio.v2 as imageio
import matplotlib.pyplot as plt
import numpy as np

def cargar_imagen_con_barra(ruta, vmin=None, vmax=None, tick_interval=50):
    """
    Carga una imagen (DICOM o raster), muestra con barra de color y devuelve numpy array.
    Normaliza si tiene rango >255 para evitar problemas al convertir a uint8.
    """
    im = imageio.imread(ruta)
    im = np.array(im)  # asegurar ndarray
    print(f"Data type: {im.dtype}")
    print(f"Shape: {im.shape}")

    # determinar rango si no se especifica
    if vmin is None: vmin = float(im.min())
    if vmax is None: vmax = float(im.max())

    # Mostrar con barra de color (no modificar los datos)
    plt.figure(figsize=(6,6))
    plt.imshow(im, vmin=vmin, vmax=vmax, cmap="gray")
    cbar = plt.colorbar()
    tick_vals = np.arange(vmin, vmax + max(1,tick_interval), tick_interval)
    cbar.set_ticks(tick_vals)
    plt.title("Imagen cargada")
    plt.axis('off')
    plt.tight_layout()
    plt.show()

    return im

