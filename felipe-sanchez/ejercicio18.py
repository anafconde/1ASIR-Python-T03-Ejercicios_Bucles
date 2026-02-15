# Autor: Felipe
# Version: 1.0
# Ejercicio 18
# Hacer un programa que muestre un cronometro, indicando las horas, minutos y segundos.

import time

hora=00
minutos=00
segundos=00

while True:
    segundos+=1
    if segundos == 60:
        segundos=0
        minutos+=1
        
    if minutos == 60:
        minutos=0
        hora+=1
    
    
    print(hora,":",minutos,":",segundos)
    time.sleep(1)