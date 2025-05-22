def piramide(n):
    i = 1
    while i <= n:
        j = 0
        letra = 65  
        fila = ""
        while j < i:
            fila = fila + chr(letra) + " "
            letra = letra + 1
            j = j + 1
        print(fila)
        i = i + 1

