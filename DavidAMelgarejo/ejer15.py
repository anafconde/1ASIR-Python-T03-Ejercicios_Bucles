"""
Una persona adquirió un producto para pagar en 20 meses. El primer mes pagó 10 €, el segundo 20 €, 
el tercero 40 € y así sucesivamente.
Realizar un algoritmo para determinar cuánto debe pagar mensualmente y el total de lo que pagó después de los 20 meses.
"""
pago=10
meses=20
pagado=10
for i in range(2,20+1):
    pago*=2
    pagado+=pago
    print(f"El mes {i} paga {pago}€")
else:
    print(f"Ha pagado {pagado}€ en total")