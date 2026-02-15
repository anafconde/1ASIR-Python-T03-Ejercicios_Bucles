# Autor: Jose Rodriguez
# Versión: 1.0
# Ejercicio 4
# Realizar un algoritmo que pida números (se pedirá por teclado la cantidad de números a introducir). 
# El programa debe informar de cuantos números introducidos son mayores que 0, menores que 0 e iguales a 0.

cantidad = int(input("¿Cuantos numeros vas a introducir?: "))

mayores = 0
menores = 0
iguales = 0

for a in range(cant):
    num = float(input(f"Introduce el numero {a + 1}: "))
    
    if num > 0:
        mayores += 1
    elif num < 0:
        menores += 1
    else :
        iguales += 1

print(f"Números mayores que 0: {mayores}")
print(f"Números menores que 0: {menores}")
print(f"Números iguales a 0: {iguales}")