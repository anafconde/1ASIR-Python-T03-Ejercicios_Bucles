# Autor: Jose Rodriguez
# Versión: 1.0
# Ejercicio 16
# Una empresa les paga a sus empleados con base en las horas trabajadas en la semana. 
# Realice un algoritmo para determinar el sueldo semanal de N trabajadores y, además, calcule cuánto pagó la empresa por los N empleados.

n = int(input("Introduce el número de trabajadores: "))

total_empresa = 0

for i in range(1, n+1):
    print("Trabajador", i)
    horas = float(input("Introduce las horas trabajadas esta semana: "))
    pago_hora = float(input("Introduce el pago por hora: "))

    sueldo = horas * pago_hora
    total_empresa = total_empresa + sueldo
    
    print("El sueldo del trabajador", i, "es:", sueldo)

    print("La empresa pagó en total:", total_empresa)
