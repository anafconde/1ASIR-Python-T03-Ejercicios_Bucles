# Autor: Felipe
# Version: 1.0
# Ejercicio 10
# Algoritmo que muestre la tabla de multiplicar de los números 1,2,3,4 y 5.


tabla=int(input("¿Que tabla deseas visualizar(1|2|3|4|5): "))

if tabla == 1:
    for i in range(1,11):
       print(tabla,"x",i,"=",tabla * i)
elif tabla == 2:
    for i in range(1,11):
       print(tabla,"x",i,"=",tabla * i)
elif tabla == 3:
    for i in range(1,11):
       print(tabla,"x",i,"=",tabla * i)
elif tabla == 4:
    for i in range(1,11):
       print(tabla,"x",i,"=",tabla * i)
elif tabla == 5:
    for i in range(1,11):
       print(tabla,"x",i,"=",tabla * i)
else:
    print("Valor introducido no es correcto: ")