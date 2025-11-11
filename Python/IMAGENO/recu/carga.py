import imageio.v2 as imageio
import matplotlib.pyplot as plt
import numpy as np

def cargar_imagen_con_barra(ruta, vmin=None, vmax=None, tick_interval=50):
    
    im = imageio.imread(ruta)
    im = np.array(im)  
    print(f"Data type: {im.dtype}")
    print(f"Shape: {im.shape}")

    if vmin is None: vmin = float(im.min())
    if vmax is None: vmax = float(im.max())

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


# EL pixel es el elemento mas pequeño al momento de formar una imagen, y nuestra imagen es una matriz de pixeles, cada pixel tiene un valor
# de intensidad como tambien de ubicaciòn, al momento de cargar la imagen y mostra la barra lateral de los niveles de iluminacion, se ve que van desde 
# 0 a 255, caracteristico de una imagen uint8 = 256 tonalidades diferentes. donde 0 es oscuro y 255 es claro a lo maximo
#Tambien se muestra el tamaño de nuestra matriz que tiene una forma de (1300, 1068), y no tiene metadatos incriptados dentro de esta imagen.

