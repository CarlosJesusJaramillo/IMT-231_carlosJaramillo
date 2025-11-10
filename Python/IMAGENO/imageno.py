from imagenoop import (
    descomprimir_zip, cargar_imagen, listar_imagenes, cargar_volumen,
    mostrar_imagen, mostrar_subplots, mostrar_cortes_planos,
    aplicar_filtros_automaticos,
    mascara_hueso, mascara_tejido, overlay_mask,
    etiquetar, media_pixeles, varianza_pixeles, histogramas_pixeles, plot_histogramas
)


def menu():
    print("\n=== MENÚ DE IMÁGENES MÉDICAS ===")
    print("1. Listar imágenes en carpeta")
    print("2. Cargar imagen")
    print("3. Aplicar filtros automáticos")
    print("4. Crear máscaras (hueso y tejido)")
    print("5. Mostrar imagen en subplots")
    print("6. Mostrar cortes planos (volumen 3D)")
    print("7. Medidas de intensidad y varianza")
    print("8. Histogramas por objeto")
    print("0. Salir")
    opcion = input("Elija una opción: ")
    return opcion


def seleccionar_imagen(carpeta):
    imgs = listar_imagenes(carpeta)
    if not imgs:
        print("No hay imágenes en la carpeta.")
        return None
    for i, img in enumerate(imgs):
        print(f"{i+1}. {img}")
    while True:
        try:
            idx = int(input("Seleccione imagen a cargar: ")) - 1
            if 0 <= idx < len(imgs):
                imagen = cargar_imagen(imgs[idx])
                print(f"Imagen cargada: {imgs[idx]}")
                return imagen
            else:
                print("Índice fuera de rango. Intente de nuevo.")
        except ValueError:
            print("Entrada inválida. Ingrese un número.")


def main():
    carpeta = "imagenes_ct"
    imagen_actual = None
    volumen_actual = None
    sampling = (1, 1, 1)  # valor por defecto para cortes 3D

    while True:
        opcion = menu()

        if opcion == "1":
            imgs = listar_imagenes(carpeta)
            if not imgs:
                print("No se encontraron imágenes.")
            for i, img in enumerate(imgs):
                print(f"{i+1}. {img}")

        elif opcion == "2":
            imagen_actual = seleccionar_imagen(carpeta)
            if imagen_actual is not None:
                mostrar_imagen(imagen_actual, titulo="Imagen cargada")

        elif opcion == "3":
            if imagen_actual is None:
                print("Primero cargue una imagen.")
                continue
            filtros = aplicar_filtros_automaticos(imagen_actual)
            for nombre, imf in filtros.items():
                print(f"Mostrando filtro: {nombre}")
                mostrar_imagen(imf, titulo=nombre)

        elif opcion == "4":
            if imagen_actual is None:
                print("Primero cargue una imagen.")
                continue
            mask_hueso = mascara_hueso(imagen_actual)
            mask_tejido = mascara_tejido(imagen_actual)
            mostrar_subplots([overlay_mask(mask_hueso), overlay_mask(mask_tejido)],
                             nrows=1, ncols=2)

        elif opcion == "5":
            if imagen_actual is None:
                print("Primero cargue una imagen.")
                continue
            mostrar_subplots([imagen_actual])

        elif opcion == "6":
            if volumen_actual is None:
                print("Cargando volumen 3D desde la carpeta...")
                volumen_actual, sampling = cargar_volumen(carpeta)
                print(f"Volumen cargado con {volumen_actual.shape[0]} cortes")
            mostrar_cortes_planos(volumen_actual, sampling)

        elif opcion == "7":
            if imagen_actual is None:
                print("Primero cargue una imagen.")
                continue
            mask = mascara_hueso(imagen_actual)
            labels, nlabels = etiquetar(mask)
            if nlabels == 0:
                print("No se detectaron objetos en la máscara.")
                continue
            print(f"Número de objetos detectados: {nlabels}")
            for i in range(1, nlabels+1):
                media = media_pixeles(imagen_actual, labels, index=i)
                var = varianza_pixeles(imagen_actual, labels, index=i)
                print(f"Objeto {i}: Media={media:.2f}, Varianza={var:.2f}")

        elif opcion == "8":
            if imagen_actual is None:
                print("Primero cargue una imagen.")
                continue
            mask = mascara_hueso(imagen_actual)
            labels, nlabels = etiquetar(mask)
            if nlabels == 0:
                print("No hay objetos para histogramas.")
                continue
            hists = histogramas_pixeles(imagen_actual, labels, index=range(1, nlabels+1))
            plot_histogramas(hists, etiquetas=range(1, nlabels+1))

        elif opcion == "0":
            print("Saliendo...")
            break

        else:
            print("Opción inválida, intente de nuevo.")


if __name__ == "__main__":
    main()
