# Autor: Felipe
# Version: 1.0
# Ejercicio 20
# Mostrar en pantalla los N primero número primos. Se pide por teclado la cantidad de números primos que queremos mostrar.

numero = int(input("¿Cuantos numeros quieres mostrar?: "))

mostrado = 0
empieza = 2

while mostrado < numero:

    es_primo = True 
    
    for i in range(2, empieza):
        if empieza % i == 0:
            es_primo = False
            break
            

    if es_primo:
        print(empieza)
        mostrado += 1

    empieza += 1