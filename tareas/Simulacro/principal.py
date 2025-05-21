from operaciones import contar,imprimir,mostrar,cantidad,es_palindromo

while True:
    print("--------------------------------- MENÚ DE OPCIONES -----------------------------------")
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
        n = int(input("Ingrese la altura de la piramide  :  "))
        imprimir(n)
        
    elif p == 3:
        n= int(input("Ingrese un numero para el cual para mostrar los primeros terminos de su serie: "))
        mostrar(n)
    
    elif p == 4:
        n=int(input("Ingrese un numero para ver la cantidad de nueros primos que tiene desde 1 hasta este : "))
        resultado = cantidad(n)
        print(f"La cantidad de numeros primos entre 1 hasta {n}, es igual a : ", resultado)
    
    elif p == 5:
        n= int(input("Ingrese un numero para verificar si su numero es palindromo: "))
        resultado = es_palindromo(n)
        print("Su numero que ha ingresado  ", resultado)
      
    
    elif p == 6:
        print("Ha seleccionado la opcion de salir de nuestro Menu de Operaciones, ¡¡Hasta luego !!")
        break
    else:
        print("Opción no válida. Intente nuevamente.")



