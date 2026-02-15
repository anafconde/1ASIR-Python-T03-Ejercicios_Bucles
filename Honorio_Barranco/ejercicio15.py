# Autor: Honorio
# Version: 1.0
#Una persona adquirió un producto para pagar en 20 meses. El primer mes pagó 10 €, el segundo 20 €, el tercero 40 € y así sucesivamente.
#Realizar un algoritmo para determinar cuánto debe pagar mensualmente y el total de lo que pagó después de los 20 meses.
import os
os.system("cls")

total_pago=0

for m in range(1,21):
    pago= 10 * (2 ** (m - 1))
    print(f"Mes {m}: {pago} €")
    total_pago = total_pago + pago
print(f"Total de lo que pago en 20 meses es de {total_pago}€")
