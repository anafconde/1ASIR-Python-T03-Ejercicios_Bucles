"""
Una empresa les paga a sus empleados con base en las horas trabajadas en la semana.
Realice un algoritmo para determinar el sueldo semanal de N trabajadores y, además, 
calcule cuánto pagó la empresa por los N empleados.
"""
horas=40
sueldo=9
while True:
    try:
        n=int(input("Numero de trabajadores: "))
        if n>0:
            print(f"El sueldo semanal por trabajdor es {horas*sueldo}\n La empresa gasto {horas*sueldo*n} en salarios esta semana por los {n} trabajadores")
            break
    except ValueError:
        print("Numero no valido")