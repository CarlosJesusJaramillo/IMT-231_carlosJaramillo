import numpy as np
import matplotlib.pyplot as plt
import scipy.ndimage as ndi

def detectar_bordes_y_segmentacion(im):
    
    imf = np.array(im, dtype=float)
    lo, hi = imf.min(), imf.max()
    if hi > lo:
        imf = (imf - lo) / (hi - lo)

    sobel_x = ndi.sobel(imf, axis=0)
    sobel_y = ndi.sobel(imf, axis=1)
    edges = np.hypot(sobel_x, sobel_y)

    
    thresh = imf.mean() + imf.std() * 0.5   
    mask_final = imf > thresh
    mask_final = ndi.binary_closing(mask_final, iterations=2)
    try:
        mask_final = ndi.binary_fill_holes(mask_final)
    except Exception:
        pass

    objeto = np.where(mask_final, imf, 0)

    fig, axes = plt.subplots(1, 4, figsize=(14,4))
    axes[0].imshow(imf, cmap='gray'); axes[0].set_title("Imagen base"); axes[0].axis('off')
    axes[1].imshow(edges, cmap='gray'); axes[1].set_title("Bordes (Sobel)"); axes[1].axis('off')
    axes[2].imshow(mask_final, cmap='gray'); axes[2].set_title("Máscara final"); axes[2].axis('off')
    axes[3].imshow(objeto, cmap='gray'); axes[3].set_title("Objeto extraído"); axes[3].axis('off')
    plt.tight_layout()
    plt.show()

    return edges, mask_final, objeto


#El metodo que se utilizo para encontrar objetos se utilizo: ndi.find_objects(labels == index) para buscar los objetos 
# y poner los labels para etiquetar cada imagen encontrada en la cual se pudo detectar una cantidad de 249 objetos en total, y 
# entre esos dar la direccion de un objeto el cual sera segmentado y mostrado como una secccion de esta. 


