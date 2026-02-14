#Autor: Alberto Jiménez Mellado
#Version: 1.0
#Mostrar en pantalla los N primeros números primos.
#Se pide por teclado la cantidad de números primos que queremos mostrar.

num = int(input("Dime la cantidad de número que quieres que se muestren los primos: "))

print ("-------------------PRIMOS O NO PRIMOS-------------------")

for i in  range (1, num + 1):
    if i % 2 == 0:
        print(f"El número {i} no es primo")
    else:
        print(f"El número {i} es primo")



