# Autor: David González Mora
# versión: 1.0
# Ejercicio 16 Relación de ejercicios
# Una empresa les paga a sus empleados con base en las horas trabajadas en la semana. Realice un algoritmo para determinar el sueldo semanal de N trabajadores y, además, calcule cuánto pagó la empresa por los N empleados.

n = int(input("Número de trabajadores: "))

total_empresa = 0

for i in range(1, n + 1):
    horas = float(input("Horas trabajadas del trabajador " + str(i) + ": "))
    pago_hora = float(input("Pago por hora del trabajador " + str(i) + ": "))
    
    sueldo = horas * pago_hora
    total_empresa = total_empresa + sueldo
    
    print("Sueldo del trabajador", i, ":", sueldo)

print("Total pagado por la empresa:", total_empresa)
