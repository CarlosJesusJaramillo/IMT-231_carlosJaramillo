import numpy as np
import matplotlib.pyplot as plt
import scipy.ndimage as ndi

def mostrar_hist_y_cdf(im):
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
    im_flat = np.array(im)
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


#Un histograma es una representacion grafica entre lo que serian nuestras intensidades y la cantidad de pixeles que la imagen cargada tiene
#La ecualizacion es un metodo en el cual se redistribuye lo que spn las intendisades de forma esten mas parejos y que se pueda observar ciertos 
# puntos que quiza se quedaron vacios y no se pudieron visualizar.
# Como tal si fuera algun tejido de mayor densidad o que tuviera estructuras en sus alrededores, se podria apreciar mejor estas, pero como es la 
#radiografia de una mano, le da mayor claridad de la imagen original y no ayudaria tanto como en otras imagenes pero funcionaria para ver las 
#falanges y parte del carpo y metacarpo.