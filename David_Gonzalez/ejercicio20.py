# Autor: David González Mora
# versión: 1.0
# Ejercicio 20 Relación de ejercicios
# Mostrar en pantalla los N primero número primos. Se pide por teclado la cantidad de números primos que queremos mostrar.

n = int(input("¿Cuántos números primos quieres mostrar? "))

contador = 0      
numero = 2        

while contador < n:
    es_primo = True
    
    for i in range(2, numero):
        if numero % i == 0:
            es_primo = False
            break
    
    if es_primo:
        print(numero)
        contador += 1
    
    numero += 1
