# Autora: Noelia López Poyatos
# Version: 1.0
# Descripción: Primeros pasos con Python
# Fecha: 2025-02-13

# Ejercicio 6: Números pares entre dos valores
# Escribir un programa que imprima todos los números pares entre dos números que se le pidan al usuario.

# Pedir al usuario los dos números
num1 = int(input("Introduce el primer número: "))
num2 = int(input("Introduce el segundo número: "))
# Asegurarse de que num1 es el menor
if num1 > num2:
    num1, num2 = num2, num1
# Imprimir los números pares entre num1 y num2
print(f"Números pares entre {num1} y {num2}:")
for i in range(num1, num2 + 1):
    if i % 2 == 0:
        print(i)

        