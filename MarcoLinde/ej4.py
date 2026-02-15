#Ejercicio 4
#Realizar un algoritmo que pida números (se pedirá por teclado la cantidad de 
#números a introducir). El programa debe informar de cuantos números 
#introducidos son mayores que 0, menores que 0 e iguales a 0.
cant= int(input("Pon la cantidad de números que quieres poner: "))
pos= 0
neg= 0
igual= 0
for i in range(cant):
    num= float(input("Pon un número: "))
    if num>0:
        pos= pos+1
    else:
        if num<0:
            neg= neg+1
        else:
            igual= igual+1
print("Mayores que 0: ", pos)
print("Menores que 0: ", neg)
print("Iguales a 0: ", igual)
