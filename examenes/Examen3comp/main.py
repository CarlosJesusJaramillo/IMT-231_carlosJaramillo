from operaciones import calcular, piramide, primar, fibonacci

while True:
    print("--------------------------------- Menu de Operaciones -----------------------------------------------")
    print("1.- Calcular la suma de todos los divisores del numero ingresado N (excluyendo el propio numero)")
    print("2.- Generar un triangulo  con letras del alfabeto hasta una altura N ingresada")
    print("3.- Mostrar los primeros N numeros primos")
    print("4.- Generar una secuencia de los primeros N términos de la serie de Fibonacci inversa")
    print("5.- Salir del menu de operaciones")
    
    op = int(input("Ingrese una opcion dentro de nuestro menu de operaciones: "))

    if op == 1:
        while True:
            n = int(input("Ingrese un numero positivo para calcular la suma de sus divisores: "))
            if n > 0:
                break
            print("Error: Ingrese un numero positivo o mayor que 0.")
        resultado = calcular(n)
        print(f"La suma de los divisores propios del numero {n} es: {resultado}")
    
    elif op == 2:
        while True:
            n = int(input("Ingrese la altura de la piramide: "))
            if n > 0:
                break
            print("Error: Ingrese un numero mayor que 0.")
        print(f"Piramide de altura {n}:")
        piramide(n)
        
    elif op == 3:
        while True:
            n = int(input("Ingrese la cantidad de numeros primos que desea visualizar: "))
            if n > 0:
                break
            print("Error: Ingrese un numero mayor que 0.")
        print(f"Los primeros {n} numeros primos son:")
        primar(n)
    


    elif op == 4:
        while True:
            n = int(input("Ingrese la cantidad de ultimos numeros que se mostraran de la serie de Fibonacci inversa: "))
            if n > 0:
                break
            print("Error: Ingrese un numero mayor que 0.")
        print(f"La serie de los ultimos numeros de cantidad {n} de Fibonacci inversa:")
        fibonacci(n)
    
    elif op == 5:
        print("Gracias por usar el programa. ¡Hasta luego!")
        break

    else:
        print("Error: se ha seleccionado una opcion que no esta dentro de nuesro menu de operaciones, seleccione otra opcion.")


