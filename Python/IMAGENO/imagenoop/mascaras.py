# imagenoop/mascaras.py
"""
Funciones para crear máscaras binarias.
Devuelven máscaras 0/1 (uint8) o booleanas según la función.
"""

import numpy as np
import matplotlib.pyplot as plt

def aplicar_mascara(imagen, umbral=128):
    """
    Aplica máscara binaria simple con un umbral dado.
    Devuelve arreglo uint8 con valores 0/1.
    """
    arr = np.asarray(imagen)
    mask = (arr >= umbral).astype(np.uint8)
    return mask

def aplicar_mascara_interactiva(imagen):
    """
    Interfaz simple por terminal: pide umbral y muestra la máscara.
    """
    while True:
        entrada = input("Ingrese umbral (0 para salir): ").strip()
        if entrada == "0":
            break
        try:
            umbral = int(entrada)
            mask = aplicar_mascara(imagen, umbral) * 255  # para visualizar mejor
            plt.imshow(mask, cmap='gray')
            plt.title(f"Máscara con umbral {umbral}")
            plt.axis('off')
            plt.show()
        except ValueError:
            print("Ingrese un número válido")
