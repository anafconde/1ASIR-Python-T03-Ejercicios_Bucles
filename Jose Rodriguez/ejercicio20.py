# Autor: Jose Rodriguez
# Versión: 1.0
# Ejercicio 20
# Mostrar en pantalla los N primero número primos. Se pide por teclado la cantidad de números primos que queremos mostrar.

numeros = int(input("Cuántos primos quieres: "))

nums = 0       
numero = 2     

while nums < numeros:
    divisores = 0
    i = 1
    while i <= numero:
        if numero % i == 0:
            divisores = divisores + 1
        i = i + 1
    
    if divisores == 2:
        print("Primo encontrado:", numero)
        nums = nums + 1
    
    numero = numero + 1
