#Ejercicio 18
#Hacer un programa que muestre un cronometro, indicando las horas, minutos y segundos.
for hora in range(0, 24):
    for min in range(0, 60):
        for seg in range(0, 60):
            print(hora, ":", min, ":", seg)
