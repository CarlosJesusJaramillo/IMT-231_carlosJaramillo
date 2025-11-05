"""Módulo de funciones relacionadas con cantidades"""

def contar(lista):
    """
    Devuelve el número de elementos de una lista
    y la suma total.
    """
    total = sum(lista)
    cantidad = len(lista)
    return cantidad, total
