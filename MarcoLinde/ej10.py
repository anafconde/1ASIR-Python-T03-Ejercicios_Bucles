#Ejercicio 10
#Algoritmo que muestre la tabla de multiplicar de los números 1,2,3,4 y 5.
for num in range(1, 6):
    print("Tabla del", num)
    for n in range(1, 11):
        print(num, "x", n, "=", num*n)
