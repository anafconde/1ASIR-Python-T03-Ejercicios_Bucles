# Autor : Victor Manuel
# Version : "1.0"
# Ejercicio 20:
# Mostrar en pantalla los N primero número primos.
# Se pide por teclado la cantidad de números primos que queremos mostrar.

n = int(input("Cuántos primos quieres: "))
encontrados = 0
num = 2

while encontrados < n:
    divisores = 0
    
    # Este for comprueba si el numero se puede dividir por otros
    for i in range(1, num + 1):
        if num % i == 0:
            divisores += 1
            
    # Si solo tiene 2 divisores (el 1 y el mismo), es primo
    if divisores == 2:
        print(f"Primo encontrado: {num}")
        encontrados += 1
        
    num += 1