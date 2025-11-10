# imagenoop/visualizacion.py
import matplotlib.pyplot as plt
import numpy as np
import math

def mostrar_imagen(im, cmap="gray", vmin=None, vmax=None, titulo=None):
    """Muestra una imagen 2D con matplotlib."""
    plt.imshow(im, cmap=cmap, vmin=vmin, vmax=vmax)
    if titulo:
        plt.title(titulo)
    plt.axis('off')
    plt.show()

def mostrar_subplots(lista_imagenes, nrows=1, ncols=None, cmap="gray", titles=None):
    """
    Muestra varias imágenes en subplots de forma dinámica.
    - lista_imagenes: lista de arrays 2D
    - nrows: número de filas
    - ncols: columnas (si None, se calcula)
    - titles: lista de títulos (opcional)
    """
    if ncols is None:
        ncols = math.ceil(len(lista_imagenes) / nrows) if nrows > 0 else len(lista_imagenes)

    fig, axes = plt.subplots(nrows=nrows, ncols=ncols, figsize=(4*ncols, 4*nrows))
    axes = np.atleast_1d(axes).ravel()

    for i, im in enumerate(lista_imagenes):
        axes[i].imshow(im, cmap=cmap)
        axes[i].axis('off')
        if titles and i < len(titles):
            axes[i].set_title(titles[i], fontsize=8)
        else:
            axes[i].set_title(f"Imagen {i+1}", fontsize=8)

    # apagar ejes sobrantes
    for j in range(len(lista_imagenes), len(axes)):
        axes[j].axis('off')

    plt.tight_layout()
    plt.show()

def mostrar_cortes_planos(vol, sampling=(1,1,1)):
    """
    Muestra cortes coronal y sagital de un volumen 3D.
    vol: numpy array (n_cortes, alto, ancho)
    sampling: (d0, d1, d2)
    """
    vol = np.asarray(vol)
    if vol.ndim != 3:
        raise ValueError("El volumen debe ser 3D (n_cortes, alto, ancho).")

    d0, d1, d2 = sampling
    im_coronal = vol[:, vol.shape[1]//2, :]
    im_sagital = vol[:, :, vol.shape[2]//2]

    asp_coronal = d0 / d2 if d2 != 0 else 1.0
    asp_sagital = d0 / d1 if d1 != 0 else 1.0

    fig, axes = plt.subplots(nrows=2, ncols=1, figsize=(6,10))
    axes[0].imshow(im_coronal, cmap='gray', aspect=asp_coronal)
    axes[0].set_title("Corte coronal (vista frontal)")
    axes[0].axis('off')
    axes[1].imshow(im_sagital, cmap='gray', aspect=asp_sagital)
    axes[1].set_title("Corte sagital (vista lateral)")
    axes[1].axis('off')
    plt.tight_layout()
    plt.show()
