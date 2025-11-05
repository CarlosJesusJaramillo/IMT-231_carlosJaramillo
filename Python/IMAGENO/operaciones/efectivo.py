"""Módulo de funciones relacionadas con cálculos de efectivo"""

def factorial(n):
    """
    Calcula el factorial de n (n!).
    Retorna 1 si n <= 1.
    """
    if n <= 1:
        return 1
    resultado = 1
    for i in range(2, n + 1):
        resultado *= i
    return resultado
