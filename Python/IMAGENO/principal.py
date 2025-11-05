"""Programa principal que usa el paquete operaciones"""

from operaciones import factorial, contar

def main():
    print("=== Ejercicio Modularizado ===\n")

    # Ejemplo de contar
    numeros = [10, 20, 30, 40]
    cantidad, total = contar(numeros)
    print(f"Números en la lista: {cantidad}, Suma total: {total}")

    # Ejemplo factorial
    n = 5
    print(f"Factorial de {n} es {factorial(n)}")

if __name__ == "__main__":
    main()

