# Autor: David González Mora
# versión: 1.0
# Ejercicio 18 Relación de ejercicios
# Hacer un programa que muestre un cronometro, indicando las horas, minutos y segundos.


import time

horas = 0
minutos = 0
segundos = 0

while True:
    print(f"{horas:02}:{minutos:02}:{segundos:02}")
    time.sleep(1)
    
    segundos += 1
    
    if segundos == 60:
        segundos = 0
        minutos += 1
        
    if minutos == 60:
        minutos = 0
        horas += 1
