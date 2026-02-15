#Autor: Alberto Jiménez Mellado
#Version: 1.0
#Una empresa les paga a sus empleados con base en las horas trabajadas en la semana.
#Realice un algoritmo para determinar el sueldo semanal de N trabajadores y, además, calcule cuánto pagó la empresa por los N empleados.

print ("--------------------------CALCULANDO SALARIOS--------------------------")

workers = int(input("Dime el número de trabajadores: "))
total = 0

for i in range(1, workers + 1):
    print(f"Trabajador {i}")
    
    h = float(input("Ingrese horas trabajadas: "))
    ph = float(input("Ingrese pago por hora: "))
    
    sueldo = h * ph
    print(f"El sueldo (semanal) del trabajador {i} es: {sueldo}")
    
    total += sueldo

print(f"La empresa ha pagado un total de: {total}")