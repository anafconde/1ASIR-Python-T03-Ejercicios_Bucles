# Autora: Noelia López Poyatos
# Version: 1.0
# Descripción: Primeros pasos con Python
# Fecha: 2025-02-13

#Ejercicio 10: Tabla de multiplicar de los primeros 5 números 
# Algoritmo que muestre la tabla de multiplicar de los números 1, 2, 3, 4 y 5.

# Tabla de multiplicar de los números 1 a 5 usando while

numero = 1  

while numero <= 5: 
    print("Tabla del", numero)
    
    i = 1  
    while i <= 10:  
        print(numero, "x", i, "=", numero * i)
        i = i + 1  
    
    print()  
    numero = numero + 1  
