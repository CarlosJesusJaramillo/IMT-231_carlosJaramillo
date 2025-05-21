# aqui se usara la funcion cantidad
def cantidad(n):
    def es_primo(num):
        if num < 2:
            return False
        for i in range(2, num):
            if num % i == 0:
                return False
        return True

    contador = 0
    for i in range(1, n + 1):
        if es_primo(i):
            contador += 1
    return contador
