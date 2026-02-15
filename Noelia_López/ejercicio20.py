# Autora: Noelia López Poyatos
# Version: 1.0
# Descripción: Primeros pasos con Python
# Fecha: 2025-02-13


# Ejercicio 20: Números primos hasta N. 
# Mostrar en pantalla los N primeros números primos.
# Se pide por teclado la cantidad de números primos que queremos mostrar.



N = int(input("¿Cuántos números primos quieres mostrar? "))

contador_primos = 0  
numero = 2           

while contador_primos < N:
    divisores = 0  
    
    i = 2
    while i < numero:
        if numero % i == 0:
            divisores = divisores + 1 
        i = i + 1    

    if divisores == 0:
        print(numero)
        contador_primos = contador_primos + 1
    
    numero = numero + 1

