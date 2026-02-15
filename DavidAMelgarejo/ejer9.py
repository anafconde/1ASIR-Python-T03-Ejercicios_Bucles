"""
Escribe un programa que, dados dos números, uno real (base) y un entero positivo (exponente),
saque por pantalla el resultado de la potencia.
No se puede utilizar el operador de potencia.
"""
while True:
    try:
        b=float(input("Numero Base: "))
        e=int(input("Exponente (entero positivo) : "))
        if e>=0:break
        else:print("No es entero positivo")
    except ValueError:
        print("No es un numero entero")
potencia=1
for i in range(e):
    potencia*=b 
print(f"La potencia de {b}^{e}= {potencia}")