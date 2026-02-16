# autor: Mario Arcos
# version: 1.0
# ejercicio 1


num = int(input("Introduce un número: "))
facto = 1

for i in range(1, num + 1):
    facto = facto * i

print("El factorial es:", facto)