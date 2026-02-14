"""
Realizar un algoritmo que muestre la tabla de multiplicar de un número introducido por teclado.
"""
while True:
    try:
        n=int(input("De qué numero quieres la tabla de multiplicar?: "))
        if n>0:break
        else: print("Entero mayor que 0")
    except ValueError:
        print("Numero no valido")
for i in range(1,11):
    print(f"{i} x {n} = {i*n}")