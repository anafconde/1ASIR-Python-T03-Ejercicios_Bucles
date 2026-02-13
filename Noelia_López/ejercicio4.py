# Autora: Noelia López Poyatos
# Version: 1.0
# Descripción: Primeros pasos con Python
# Fecha: 2025-02-13

# Ejercicio 4: Contar números positivos, negativos e iguales a cero 
# Realizar un algoritmo que pida números (se pedirá por teclado la cantidad de números a introducir).
#El programa debe informar de cuántos números introducidos son mayores que 0, menores que 0 e iguales a 0.
cantidad = int(input("¿Cuántos números quieres introducir? "))
positivos = 0
negativos = 0
ceros = 0
for i in range(cantidad):
    número = float(input(f"Introduce el número {i+1}: "))
    if número > 0:
        positivos += 1
    elif número < 0:
        negativos += 1
    else:
        ceros += 1
print(f"Números mayores que 0: {positivos}")
print(f"Números menores que 0: {negativos}")
print(f"Números iguales a 0: {ceros}")
