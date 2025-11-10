import os
import numpy as np
import matplotlib.pyplot as plt

from opexamen.carga import cargar_imagen_dicom
from opexamen.histogramas import calcular_histograma, ecualizar_histograma, plot_histogram_cdf

from opexamen.filtros import filtro_gaussiano, filtro_promedio, filtro_unsharp
from opexamen.bordes import sobel_magnitud, laplaciano
from opexamen import __init__ as pkg_init 

OUTDIR = os.path.join("opexamen", "output")
os.makedirs(OUTDIR, exist_ok=True)


RUTAS_POSIBLES = [
    "imagenE2.dcm",
    os.path.join("opexamen", "imagenE2.dcm"),
    os.path.join("Data", "imagenE2.dcm")
]

def encontrar_imagen():
    for p in RUTAS_POSIBLES:
        if os.path.exists(p):
            return p
    raise FileNotFoundError("No encontré imagenE2.dcm en las rutas esperadas. Coloca el archivo en la raíz, opexamen/ o Data/.")

def guardar(fig, nombre):
    ruta = os.path.join(OUTDIR, nombre)
    fig.savefig(ruta, bbox_inches='tight', dpi=150)
    print("[guardado]", ruta)

def mostrar_y_guardar_im(im, titulo, nombre_archivo):
    fig = plt.figure(figsize=(6,6))
    plt.imshow(im, cmap='gray', vmin=0, vmax=255)
    plt.title(titulo)
    plt.axis('off')
    plt.show()
    guardar(fig, nombre_archivo)

def main():
    ruta = encontrar_imagen()
    print("Cargando imagen:", ruta)
    im, meta = cargar_imagen_dicom(ruta)

    
    print("\n--- 2.1 Carga y visualización inicial ---")
    print("Forma:", im.shape)
    print("Tipo de dato:", im.dtype)
    print("Metadatos (parciales):")
    for k,v in meta.items():
        print(f"  {k}: {v}")
   
    mostrar_y_guardar_im(im, "Imagen original (gris)", "01_imagen_original.png")

    
    print("\n--- 2.2 Análisis de intensidades ---")
    fig_hist = plot_histogram_cdf(im, savepath=os.path.join(OUTDIR, "02_hist_cdf_original.png"))
    guardar(fig_hist, "02_hist_cdf_original.png")
    im_eq, hist_orig, cdf_orig = ecualizar_histograma(im)
    mostrar_y_guardar_im(im_eq, "Imagen ecualizada", "03_imagen_ecualizada.png")
    print("Comparación estadística (usa esto en tu informe):")
    print(f"  Media original: {float(np.mean(im)):.2f}, Desv.std original: {float(np.std(im)):.2f}")
    print(f"  Media ecualizada: {float(np.mean(im_eq)):.2f}, Desv.std ecualizada: {float(np.std(im_eq)):.2f}")
    

    


    print("\n--- 2.4 Filtrado (suavizado y realce) ---")
    im_gauss = filtro_gaussiano(im, sigma=1.0)
    im_prom = filtro_promedio(im, size=3)
    im_unsharp = filtro_unsharp(im, sigma=1.0, amount=1.2)
    im_sobel = sobel_magnitud(im)

    fig2, axes2 = plt.subplots(2,2, figsize=(10,8))
    axes2[0,0].imshow(im, cmap='gray'); axes2[0,0].set_title("Original"); axes2[0,0].axis('off')
    axes2[0,1].imshow(im_gauss, cmap='gray'); axes2[0,1].set_title("Gaussiano σ=1"); axes2[0,1].axis('off')
    axes2[1,0].imshow(im_prom, cmap='gray'); axes2[1,0].set_title("Promedio 3x3"); axes2[1,0].axis('off')
    axes2[1,1].imshow(im_unsharp, cmap='gray'); axes2[1,1].set_title("Unsharp "); axes2[1,1].axis('off')
    plt.tight_layout(); plt.show()
    guardar(fig2, "05_filtros_grid.png")
    
    fig_sobel = plt.figure(figsize=(6,6))
    plt.imshow(im_sobel, cmap='gray'); plt.title("Sobel"); plt.axis('off'); plt.show()
    guardar(fig_sobel, "06_sobel.png")
    

    
    print("\n--- 2.5 Detección de bordes, segmentación y extracción ---")
    
    mask_final = mask_adj
   
    labels, nlabels = ndi_label(mask_final)
    print("Objetos detectados:", nlabels)
    if nlabels > 0:
        
        areas = np.array([np.sum(labels == (i+1)) for i in range(nlabels)])
        idx_max = int(np.argmax(areas)) + 1
        bboxes = np.array(ndi_find_objects(labels))
    
        bbox = ndi_find_objects(labels)[idx_max-1]
        im_crop = im[bbox]
        
        fig_crop = plt.figure(figsize=(5,5)); plt.imshow(im_crop, cmap='gray'); plt.title(f"Crop objeto {idx_max}"); plt.axis('off'); plt.show()
        guardar(fig_crop, f"07_crop_obj_{idx_max}.png")
        
        mean_obj = np.mean(im[labels == idx_max])
        var_obj = np.var(im[labels == idx_max])
        print(f"Objeto {idx_max}: media={mean_obj:.2f}, varianza={var_obj:.2f}")
    else:
        print("No se detectó ningún objeto en la máscara final.")

    



import scipy.ndimage as _ndi
def ndi_label(mask):
    return _ndi.label(mask)
def ndi_find_objects(labels):
    return _ndi.find_objects(labels)

if __name__ == "__main__":
    main()
