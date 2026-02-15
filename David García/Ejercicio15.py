# Author: David García Pérez
# Version: 1.0

# Ejercicio 15
# Una persona adquirió un producto para pagar en 20 meses.
# El primer mes pagó 10 €, el segundo 20 €, el tercero 40 € y así sucesivamente.
# Realizar un algoritmo para determinar cuánto debe pagar mensualmente y el total de lo que pagó después de los 20 meses.

import os
os.system("cls")

print(" ")
print("#################### Calcular cuota mensual y total a pagar ######################")
print(" ")

meses = 20
pago = 10
total = 0

for mes in range(1, meses + 1):
    print(f"Mes {mes}: {pago} €")
    total = total + pago
    pago = pago * 2

print(f"Total pagado después de {meses} meses: {total} €")

print(" ")
print("#################### Fin del programa ######################")
print(" ")