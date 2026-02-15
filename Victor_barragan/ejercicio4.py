# Autor : Victor Manuel
# Version : "1.0"
# Ejercicio 4:
# Realizar un algoritmo que pida números 
# (se pedirá por teclado la cantidad de números a introducir).
# El programa debe informar de cuántos números introducidos son mayores que 0,
# menores que 0 e iguales a 0.

cant = int(input("Cuantos numero vas a introudir: "))

# 2. Inicializamos los contadores en cero
Mayores = 0
Menores = 0
Iguales = 0

for i in range(cant):
    num = float(input(f"Introduce el numero {i + 1}: "))
    
    if num > 0:
        Mayores += 1
    elif num < 0:
        Menores += 1
    else :
        Iguales += 1

print(f"Números mayores que 0: {Mayores}")
print(f"Números menores que 0: {Menores}")
print(f"Números iguales a 0: {Iguales}")
