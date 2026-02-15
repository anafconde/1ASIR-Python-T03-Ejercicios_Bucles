# Autor : Victor Manuel
# Version : "1.0"
# Ejercicio 6:
# Escribir un programa que imprima 
# todos los números pares entre dos números que se le pidan al usuario.


num = int(input("En que numero quieres empezar para contar numeros pares: "))
num1 = int(input("Hasta que numero quieres llegar para contar numeros pares: "))

for i in range(num,num1 + 1):
    if i % 2 == 0 :
        print(f"numeros pares: {i}")