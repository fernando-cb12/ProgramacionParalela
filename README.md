# Suma de Números Primos menores a 5,000,000

Este proyecto implementa un programa en Python que calcula la **suma de todos los números primos menores a 5,000,000**, utilizando dos enfoques:

- Una versión **secuencial**
- Una versión **paralela** utilizando `multiprocessing`

El resultado esperado es: `838,596,693,108`.

---

## 🧠 Algoritmo para verificar si un número es primo

Se utiliza un algoritmo sencillo pero intensivo para el CPU:

1. Si `n` < 2, no es primo.
2. Para `i` desde 2 hasta `√n`:
   - Si `n` es divisible por `i`, no es primo.
   - Si no, se sigue con el siguiente `i`.
3. Si el ciclo termina normalmente, `n` es primo.

Este algoritmo se aplica en ambas versiones.

---

## Resultados de ejecución

### Versión secuencial

```bash
Resultado: 838596693108
Tiempo: 24.80356502532959 segundos
```

### Versión paralela

```bash
Resultado: 838596693108
Tiempo: 4.8457605838775635 segundos
```
