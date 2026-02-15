# Autora: Noelia López Poyatos
# Version: 1.0
# Descripción: Primeros pasos con Python
# Fecha: 2025-02-13

# Ejercicio 16: Sueldo semanal de empleados. 
# Una empresa les paga a sus empleados con base en las horas trabajadas en la semana.
# Realice un algoritmo para determinar el sueldo semanal de N trabajadores y, además, calcule cuánto pagó la empresa por los N empleados.


N = int(input("¿Cuántos empleados hay? "))
total_empresa = 0  
empleado = 1       

while empleado <= N:
    horas = float(input("Introduce las horas trabajadas del empleado " + str(empleado) + ": "))
    sueldo = horas * 10  
    print("El sueldo del empleado", empleado, "es:", sueldo, "euros")
    
    total_empresa = total_empresa + sueldo  
    empleado = empleado + 1  

print("La empresa pagó en total:", total_empresa, "euros")
