# Autor: Felipe
# Version: 1.0
# Ejercicio 4
# Realizar un algoritmo que pida números (se pedirá por teclado la cantidad de números a introducir). 
# El programa debe informar de cuantos números introducidos son mayores que 0, menores que 0 e iguales a 0.

pedidos=int(input("¿Cuantos numero quieres introducir?: "))

mayor=0
menor=0
igual=0

for n in range(pedidos):
    numero=int(input("Dame un numero: "))
    
    if numero > 0:
        mayor += 1
    elif numero < 0:
        menor += 1
    else:
        igual += 1

print("Numeros mayores que 0: ",mayor)
print("Numeros menores que 0: ",menor)
print("Numeros iguales que 0: ",igual)