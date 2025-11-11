import os
import matplotlib.pyplot as plt
from scipy.ndimage import label
from recupera import *

OUTDIR = os.path.join("recupera", "output")
os.makedirs(OUTDIR, exist_ok=True)
RUTA_IMAGEN = "imagenE2.dcm"

def mostrar_imagen(im, titulo):
    plt.figure(figsize=(6,6))
    plt.imshow(im, cmap='gray', vmin=0, vmax=255)
    plt.title(titulo)
    plt.axis('off')
    plt.show()

def main():
    # Cargar imagen
    im, meta = cargar_imagen_dicom(RUTA_IMAGEN)
    print("Forma:", im.shape)
    print("Tipo de dato:", im.dtype)
    print("Metadatos:", meta)
    mostrar_imagen(im, "Imagen original")

    # Histogramas
    plot_histogram(im, "Histograma original")
    plot_histogram_cdf(im, "Histograma y CDF original")

    # Ecualización
    im_eq = ecualizar_histograma(im)
    mostrar_imagen(im_eq, "Imagen ecualizada")
    plot_histogram(im_eq, "Histograma ecualizado")
    plot_histogram_cdf(im_eq, "Histograma y CDF ecualizado")

    # Máscaras Otsu
    umbral = otsu_umbral(im)
    mask = umbral_simple(im, umbral)
    mask_adj = ajustar_mascara(mask, operacion='closing', size=3)

    plt.figure(figsize=(10,5))
    plt.subplot(1,2,1); plt.imshow(mask, cmap='gray'); plt.title("Máscara Otsu")
    plt.subplot(1,2,2); plt.imshow(mask_adj, cmap='gray'); plt.title("Máscara ajustada")
    plt.show()

    # Filtros
    im_gauss = filtro_gaussiano(im, sigma=1)
    im_prom = filtro_promedio(im, size=3)
    im_unsharp = filtro_unsharp(im, sigma=1, amount=1.2)
    im_sobel = sobel_magnitud(im)
    im_lap = laplaciano(im)

    plt.figure(figsize=(10,8))
    plt.subplot(2,3,1); plt.imshow(im, cmap='gray'); plt.title("Original")
    plt.subplot(2,3,2); plt.imshow(im_gauss, cmap='gray'); plt.title("Gaussiano")
    plt.subplot(2,3,3); plt.imshow(im_prom, cmap='gray'); plt.title("Promedio")
    plt.subplot(2,3,4); plt.imshow(im_unsharp, cmap='gray'); plt.title("Unsharp")
    plt.subplot(2,3,5); plt.imshow(im_sobel, cmap='gray'); plt.title("Sobel")
    plt.subplot(2,3,6); plt.imshow(im_lap, cmap='gray'); plt.title("Laplaciano")
    plt.tight_layout(); plt.show()

    # Segmentación y extracción de objeto
    im_objeto, mask_final = segmentar_y_extraer_objeto(im, metodo_borde='sobel', operacion='closing', size=3, mostrar=True)

    if im_objeto is not None:
        labels_mask, nlabels = label(mask_final)
        areas = [np.sum(labels_mask==i+1) for i in range(nlabels)]
        idx_max = int(np.argmax(areas)) + 1
        mean_obj = im[labels_mask==idx_max].mean()
        var_obj = im[labels_mask==idx_max].var()
        print(f"Objeto {idx_max}: media={mean_obj:.2f}, varianza={var_obj:.2f}")

if __name__ == "__main__":
    main()

