inf = int(input("Límite inferior: "))
sup = int(input("Límite superior: "))

while inf >= sup:
    print("Error: el inferior debe ser menor que el superior.")
    inf = int(input("Límite inferior: "))
    sup = int(input("Límite superior: "))

suma_dentro = 0
fuera = 0
igual_limite = False

num = int(input("Introduce un número (0 para salir): "))
while num != 0:
    if num > inf and num < sup:
        suma_dentro += num
    else:
        fuera += 1
    
    if num == inf or num == sup:
        igual_limite = True
    
    num = int(input("Introduce otro número (0 para salir): "))

print("Suma:", suma_dentro)
print("Números que se quedan fuera:", fuera)
if igual_limite:
    print("Se ha introducido un número dentro de los límites.")
else:
    print("No se ha introducido números iguales a los límites.")