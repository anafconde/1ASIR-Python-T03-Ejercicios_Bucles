# Autor: David González Mora
# versión: 1.0
# Ejercicio 10 Relación de ejercicios
# Algoritmo que muestre la tabla de multiplicar de los números 1,2,3,4 y 5.

for i in range(1, 6):
    print("Tabla del", i)
    
    for j in range(1, 11):     
        print(i, "x", j, "=", i * j)
    
