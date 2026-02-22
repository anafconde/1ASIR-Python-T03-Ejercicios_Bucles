#Una persona adquirió un producto para pagar en 20 meses . El primer mes pagó 10€, el segundo 20€, el tercero 40€ y así sucesivamente.
#Realice un algoritmo para determinar cuánto debe mensualmente y el total de lo que pagó después de los 20 meses.
pago_mensual=10
producto =int(input("introduce el repcio del producto "))
precio_final=0
for p in range(1,21):
	precio_final=precio_final+pago_mensual
	pago_mensual=pago_mensual*2
	print("el pago mensual del mes", p, "es de", pago_mensual, "euros")