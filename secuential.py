import math
import time

def es_primo(n):
    if n < 2:
        return False
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True



def suma_primos_secuencial(limite):
    suma = 0
    for n in range(2, limite):
        if es_primo(n):
            suma += n
    return suma

# Ejecutar y medir tiempo
inicio = time.time()
resultado = suma_primos_secuencial(5_000_000)
fin = time.time()

print("Resultado:", resultado)
print("Tiempo secuencial:", fin - inicio, "segundos")
