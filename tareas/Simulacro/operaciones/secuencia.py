#funcion usada mostrar: 
def mostrar(n):
    secuencia = []
    for i in range(1, n + 1):
        secuencia.append(str(i if i % 2 != 0 else -i))
    print(", ".join(secuencia))
