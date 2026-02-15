# Autor: Jose Rodriguez
# Versión: 1.0
# Ejercicio 18
# Hacer un programa que muestre un cronometro, indicando las horas, minutos y segundos.

import time

for h in range(24):
    for m in range(60):
        for s in range(60):
            print(f"Cronometro {h}:{m}:{s}")
            time.sleep(1)