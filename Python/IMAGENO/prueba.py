# función que calcula el factorial de un número
def
/*************  ✨ Windsurf Command ⭐  *************/
def factorial(n):
    """
    Calcula el factorial de n (n!).
    Retorna 1 si n <= 1.
    """
    if n <= 1:
/*************  ✨ Windsurf Command 🌟  *************/
        return 1

def mostrar_histograma_cdf(im, bins=256):
    """
    Muestra el histograma y la función de distribución acumulativa (CDF) de una imagen.

    Parámetros:
    -----------
    im : numpy array
        Imagen 2D de intensidad (uint8 o similar)
    bins : int
        Número de bins para el histograma (por defecto 256)
    """
    # Asegurarse que la imagen es numpy array
    im = np.array(im)

    # Histograma
    hist = ndi.histogram(im, min=0, max=255, bins=bins)

    # CDF normalizada
    cdf = hist.cumsum() / hist.sum()

    # Graficar
    fig, axes = plt.subplots(2, 1, figsize=(8,6), sharex=True)
    axes[0].plot(hist, color='blue', label='histograma')
    axes[0].set_ylabel("Número de píxeles")
    axes[0].legend(loc='upper right')

    axes[1].plot(cdf, color='red', label='CDF')
    axes[1].set_xlabel("Intensidad")
    axes[1].set_ylabel("Proporción acumulada")
    axes[1].legend(loc='upper right')

    plt.tight_layout()
    plt.show()
/*******  4ee1363f-13db-46f7-8fa8-4c9af4f6e972  *******/
    resultado = 1
    for i in range(2, n + 1):
        resultado *= i
    return resultado
/*******  644cf858-ff5b-4bc4-851f-4eedbb72f98d  *******/
BlockingIOError
# quiero que me ayudes a hacer un codigo que vea los numeros primos
def


/*************  ✨ Windsurf Command ⭐  *************/
def es_primo(n):
    """
    Comprueba si un número es primo.
    """
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True
/*******  369a1753-d2e1-43c3-975f-97716b80d897  *******/



