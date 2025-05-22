def primar(n):
    cantidad = 0
    numero = 2

    while cantidad < n:
        es_primo = True
        divisor = 2
        while divisor < numero:
            if numero % divisor == 0:
                es_primo = False
                break
            divisor = divisor + 1

        if es_primo:
            print(numero)
            cantidad = cantidad + 1

        numero = numero + 1


