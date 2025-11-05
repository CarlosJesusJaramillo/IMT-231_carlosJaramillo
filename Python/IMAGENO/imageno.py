from imagenooperaciones import (
    cargar_imagen_dicom, listar_dicoms, calcular_histograma, calcular_cdf, ecualizar_imagen,
    mostrar_histograma_cdf, segmentar_hueso_piel, aplicar_mascara, filtro_media
)
import matplotlib.pyplot as plt

def main():
    print("=== Bienvenido al sistema de Imagenología Médica ===\n")

    # Listar todos los DICOM disponibles en Data
    dicoms = listar_dicoms("Data")
    if not dicoms:
        print("No se encontraron archivos DICOM en la carpeta 'Data'.")
        return

    # Mostrar opciones de imágenes
    print("Seleccione una imagen DICOM para procesar:")
    for i, ruta in enumerate(dicoms, 1):
        print(f"{i}. {ruta}")

    seleccion = int(input("Ingrese el número de la imagen: ")) - 1
    if seleccion < 0 or seleccion >= len(dicoms):
        print("Selección inválida.")
        return

    im = cargar_imagen_dicom(dicoms[seleccion])
    print(f"Imagen cargada: {im.shape}, tipo: {im.dtype}")

    while True:
        print("\nOpciones disponibles:")
        print("1. Mostrar imagen original")
        print("2. Histograma y CDF")
        print("3. Ecualización")
        print("4. Máscaras de piel y hueso")
        print("5. Filtrado de media")
        print("6. Salir")

        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            plt.imshow(im, cmap='gray')
            plt.title("Imagen original")
            plt.show()

        elif opcion == "2":
            hist = calcular_histograma(im)
            cdf = calcular_cdf(hist)
            mostrar_histograma_cdf(hist, cdf)

        elif opcion == "3":
            hist = calcular_histograma(im)
            cdf = calcular_cdf(hist)
            im_eq = ecualizar_imagen(im, cdf)
            plt.imshow(im_eq, cmap='gray')
            plt.title("Imagen ecualizada")
            plt.show()

        elif opcion == "4":
            hist = calcular_histograma(im)
            cdf = calcular_cdf(hist)
            im_eq = ecualizar_imagen(im, cdf)
            mask_skin, mask_bone = segmentar_hueso_piel(im_eq)
            fig, axes = plt.subplots(1, 2)
            axes[0].imshow(mask_skin, cmap='gray')
            axes[0].set_title("Piel")
            axes[1].imshow(mask_bone, cmap='gray')
            axes[1].set_title("Hueso")
            plt.show()

        elif opcion == "5":
            im_filt = filtro_media(im)
            fig, axes = plt.subplots(1, 2)
            axes[0].imshow(im, cmap='gray')
            axes[0].set_title("Original")
            axes[1].imshow(im_filt, cmap='gray')
            axes[1].set_title("Filtrado")
            plt.show()

        elif opcion == "6":
            print("Saliendo del programa...")
            break

        else:
            print("Opción inválida. Intente de nuevo.")

if __name__ == "__main__":
    main()
