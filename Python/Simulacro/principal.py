from operaciones import contar#,imprimir,mostrar,cantidad,es_palindromo

while True:
    print("\n--------------------------------- MENÚ DE OPCIONES -----------------------------------n")
    print("1. Contar cuántos números entre 1 y N son divisibles por 3 o terminan en 3.")
    print("2. Imprimir una pirámide de asteriscos de altura N.")
    print("3. Mostrar los primeros N términos de la serie: 1, -2, 3, -4, 5, -6, ...")
    print("4. Mostrar la cantidad de números primos entre 1 y N.")
    print("5. Verificar si un número es palíndromo (capicúa).")
    print("6. Salir del programa.")
    p = int(input("Seleccione una opción para realizar dentro de nuestro menú de operaciones: "))

    if p == 1:
        n = int(input("Ingrese un numero para la operacion :  "))
        resultado = contar(n)
        print(f"El numero de numeros entre 1 y {n} es : ",resultado)
        
    elif p == 2:
        print("Haz seleccionado la opcion de la piramide :  ")
        resultado = imprimir
        print(resultado)
        
    elif p == 3:
        b = int(input("Ingrese un numero para el cual para mostrar los primeros terminos de su serie: "))
        resultado = mostrar(b)
        print(".")
    
    elif p == 4:
        c = int(input("Ingrese un numero para ver la cantidad de nueros primos que tiene desde 1 hasta este : "))
        resultado = cantidad
        print(f"La cantidad de numeros primos entre 1 hasta {c}, es igual a : ", resultado)
    
    elif p == 5:
        d = int(input("Ingrese un numero para verificar si su numero es palindromo"))
        resultado = es_palindromo(d)
        print("Su numero que ha ingresado es  ", resultado)
    
    
    elif p == 6:
        print("Saliendo del programa...")
        break
    else:
        print("Opción no válida. Intente nuevamente.")



