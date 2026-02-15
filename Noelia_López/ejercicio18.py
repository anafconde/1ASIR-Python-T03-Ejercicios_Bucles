# Autora: Noelia López Poyatos
# Version: 1.0
# Descripción: Primeros pasos con Python
# Fecha: 2025-02-13

# Ejercicio 18: Cronómetro. 
# Hacer un programa que muestre un cronómetro, indicando las horas, minutos y segundos.



horas = 0
minutos = 0
segundos = 0

while True:
    print(horas, ":", minutos, ":", segundos)
    
    segundos = segundos + 1
    
    if segundos == 60:  
        segundos = 0
        minutos = minutos + 1
    
    if minutos == 60:  
        minutos = 0
        horas = horas + 1

