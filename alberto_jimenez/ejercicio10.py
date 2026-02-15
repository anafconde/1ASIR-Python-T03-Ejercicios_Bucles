#Autor: Alberto Jiménez Mellado
#Version: 1.0
#Algoritmo que muestre la tabla de multiplicar de los números 1, 2, 3, 4 y 5.

num = 2

print("--------------TABLA DE MULTIPLICAR--------------")
while num >= 1 and num <= 5:
    num = int(input("Dime el número que quieras del 1 al 5: "))
    for i in range(11):
        i *= num
        print (i)