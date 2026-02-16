# Autor: Paco Fernandez
# Version: 1.0
# Una persona adquirió un producto para pagar en 20 meses. 
# El primer mes pagó 10 €, el segundo 20 €, el tercero 40 € y así sucesivamente. 
# Realizar un algoritmo para determinar cuánto debe pagar mensualmente y 
# el total de lo que pagó después de los 20 meses.

meses = 20
pago = 10  
total = 0

for mes in range(1, meses + 1):
    print(f"Mes {mes}: {pago} €")
    total = total + pago
    pago = pago * 2

print(f"Total pagado después de 20 meses: {total} €")
