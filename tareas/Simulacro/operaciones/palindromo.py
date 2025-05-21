#aqui se usara la funcion es_palindromo
def es_palindromo(num):
    if num <= 0:
        return "Error, debe ingresar un numero mayor a 0."

    if str(num) == str(num)[::-1]:
        return "es palíndromo"
    else:
        return "no es palíndromo"
