# Autor: Paco Fernandez
# Version: 1.0
# Realizar una algoritmo que muestre la tabla de multiplicar de un número introducido por teclado.

numero = int(input("Introduce el numero para obtener la tabla de multiplicar: "))
print(f"Tabla de multiplicar del {numero}")
for p in range(1,11):
    resultado = p * numero
    print(f"{p} x {numero} = {resultado} ")

