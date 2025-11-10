# pracimageno.py
from imagenoop import *
import matplotlib.pyplot as plt
import numpy as np
import math

def menu():
    print("\n=== MENÚ DE IMÁGENES MÉDICAS ===")
    print("1. Listar imágenes en carpeta")
    print("2. Cargar imagen")
    print("3. Aplicar filtros automáticos")
    print("4. Crear máscaras interactivo (umbral)")
    print("5. Mostrar imagen en subplots")
    print("6. Mostrar cortes planos (volumen 3D)")
    print("7. Medidas de intensidad y varianza (por objetos con umbral)")
    print("8. Histogramas por objeto (requiere umbral)")
    print("9. Histograma global y CDF (toda la imagen)")
    print("0. Salir")
    return input("Elija una opción: ")

def seleccionar_imagen(carpeta):
    imgs = listar_imagenes(carpeta)
    if not imgs:
        print("No se encontraron imágenes en la carpeta.")
        return None

    print("\nSeleccione una imagen:")
    for i, img in enumerate(imgs, 1):
        print(f"{i}. {img}")
    while True:
        try:
            idx = int(input("Número de imagen: ")) - 1
            if 0 <= idx < len(imgs):
                im = cargar_imagen(imgs[idx])
                return im, imgs[idx]
            else:
                print("Índice fuera de rango. Intente de nuevo.")
        except ValueError:
            print("Entrada inválida. Ingrese un número.")

def pedir_umbral(prompt="Umbral (entero, 0 para cancelar): "):
    """Pide un umbral entero y valida la entrada."""
    while True:
        s = input(prompt)
        try:
            val = int(s)
            return val
        except ValueError:
            print("Entrada inválida. Ingrese un número entero.")

def main():
    carpeta = "Data"  # carpeta por defecto
    imagen_actual = None
    nombre_imagen = ""
    volumen_actual = None
    sampling = (1,1,1)

    while True:
        opcion = menu().strip()

        if opcion == "1":
            imgs = listar_imagenes(carpeta)
            if not imgs:
                print("No hay imágenes en la carpeta.")
                continue
            print("\nImágenes disponibles:")
            for i, img in enumerate(imgs, 1):
                print(f"{i}. {img}")

        elif opcion == "2":
            resultado = seleccionar_imagen(carpeta)
            if resultado:
                imagen_actual, nombre_imagen = resultado
                print(f"Imagen cargada: {nombre_imagen}")
                mostrar_imagen(imagen_actual, titulo="Imagen cargada")

        elif opcion == "3":
            if imagen_actual is None:
                print("Primero cargue una imagen.")
                continue
            filtros = aplicar_filtros_automaticos(imagen_actual)
            nombres = list(filtros.keys())
            imgs = list(filtros.values())
            n = len(imgs)
            cols = min(4, n)
            rows = math.ceil(n / cols)
            fig, axes = plt.subplots(rows, cols, figsize=(4*cols, 3*rows))
            axes = np.atleast_1d(axes).ravel()
            for i, ax in enumerate(axes):
                if i < n:
                    ax.imshow(imgs[i], cmap='gray')
                    ax.set_title(nombres[i], fontsize=8)
                ax.axis('off')
            plt.tight_layout()
            plt.show()

        elif opcion == "4":
            if imagen_actual is None:
                print("Primero cargue una imagen.")
                continue
            print("Creación de máscara: ingrese umbral entero (0 para cancelar).")
            while True:
                umbral = pedir_umbral()
                if umbral == 0:
                    break
                mask = aplicar_mascara(imagen_actual, umbral)
                mostrar_subplots([mask*255], nrows=1, titles=[f"Mask umbral={umbral}"])

        elif opcion == "5":
            if imagen_actual is None:
                print("Primero cargue una imagen.")
                continue
            mostrar_subplots([imagen_actual], nrows=1, titles=["Imagen actual"])

        elif opcion == "6":
            if volumen_actual is None:
                print("Cargando volumen 3D desde la carpeta...")
                try:
                    res_vol, res_sampling = cargar_volumen(carpeta)
                    volumen_actual = res_vol
                    sampling = res_sampling
                except Exception as e:
                    print("Error cargando volumen:", e)
                    volumen_actual = None
                    continue
                if volumen_actual is None:
                    print("No se encontró volumen.")
                    continue
                print(f"Volumen cargado con {volumen_actual.shape[0]} cortes (shape {volumen_actual.shape})")
            mostrar_cortes_planos(volumen_actual, sampling)

        elif opcion == "7":
            if imagen_actual is None:
                print("Primero cargue una imagen.")
                continue
            print("Medición: ingrese umbral entero para segmentar objetos (0 para cancelar).")
            while True:
                umbral = pedir_umbral()
                if umbral == 0:
                    break
                mask = aplicar_mascara(imagen_actual, umbral)
                labels, nlabels = etiquetar(mask)
                if nlabels == 0:
                    print("No se detectaron objetos con ese umbral.")
                    continue
                print(f"Número de objetos detectados: {nlabels}")
                for i in range(1, nlabels + 1):
                    media = media_pixeles(imagen_actual, labels, i)
                    var = varianza_pixeles(imagen_actual, labels, i)
                    media_str = f"{media:.2f}" if (not np.isnan(media)) else "nan"
                    var_str = f"{var:.2f}" if (not np.isnan(var)) else "nan"
                    print(f"Objeto {i}: Media={media_str}, Varianza={var_str}")

        elif opcion == "8":
            if imagen_actual is None:
                print("Primero cargue una imagen.")
                continue
            print("Histogramas por objeto: ingrese umbral entero (0 para cancelar).")
            while True:
                umbral = pedir_umbral()
                if umbral == 0:
                    break
                mask = aplicar_mascara(imagen_actual, umbral)
                labels, nlabels = etiquetar(mask)
                if nlabels == 0:
                    print("No se detectaron objetos con ese umbral.")
                    continue
                hists = histogramas_pixeles(imagen_actual, min_val=0, max_val=255, bins=256, labels=labels, index=range(1, nlabels+1))
                if hists is None or len(hists) == 0:
                    print("No se pudieron calcular histogramas.")
                else:
                    plot_histogramas(hists, etiquetas=list(range(1, nlabels+1)))
                break

        elif opcion == "9":
            if imagen_actual is None:
                print("Primero cargue una imagen.")
                continue
            try:
                mostrar_histograma_cdf(imagen_actual, bins=256)
            except Exception as e:
                print("Error al generar histograma global:", e)

        elif opcion == "0":
            print("Saliendo...")
            break

        else:
            print("Opción inválida. Intente de nuevo.")


if __name__ == "__main__":
    main()
