import math
import time
import multiprocessing

def es_primo(n):
    if n < 2:
        return False
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True


def worker_primo(n):
    return n if es_primo(n) else 0

def suma_primos_paralelo(limite):
    with multiprocessing.Pool() as pool:
        resultados = pool.map(worker_primo, range(2, limite))
    return sum(resultados)

# Ejecutar y medir tiempo
if __name__ == "__main__":
    inicio = time.time()
    resultado = suma_primos_paralelo(5_000_000)
    fin = time.time()

    print("Resultado:", resultado)
    print("Tiempo paralelo:", fin - inicio, "segundos")
