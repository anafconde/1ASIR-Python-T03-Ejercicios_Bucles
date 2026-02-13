cantidad = int(input("¿Cuántos números vas a introducir?: "))
positivos = 0
negativos = 0
ceros = 0

for i in range(cantidad):
    num = int(input("Dime un número: "))
    if num > 0:
        positivos += 1
    elif num < 0:
        negativos += 1
    else:
        ceros += 1

print("Positivos:", positivos)
print("Negativos:", negativos)
print("Iguales a cero:", ceros)