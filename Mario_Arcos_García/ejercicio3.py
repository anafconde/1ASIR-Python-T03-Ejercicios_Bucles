# autor: Mario Arcos
# version: 1.0
# ejercicio 3


sum = 0
contar = 0
num = -1 

print("Introduce números (el 0 detiene el programa):")

while num != 0:
    num = float(input("Número: "))
    
    if num != 0:
        sum = sum + num
        contar = contar + 1

if contar > 0:
    media = sum / contar
    print("La suma total es:", sum)
    print("La media es:", media)
else:
    print("No pusiste ningun número antes del cero.")