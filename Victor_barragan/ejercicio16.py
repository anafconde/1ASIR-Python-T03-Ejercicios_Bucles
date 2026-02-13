# Autor : Victor Manuel
# Version : "1.0"
# Ejercicio 16: 
# Una empresa les paga a sus empleados con base en las horas trabajadas en la semana.
# Realice un algoritmo para determinar el sueldo semanal de N trabajadores y, 
# además, calcule cuánto pagó la empresa por los N empleados.

nt = int(input("Numero de trabajadores de la empresa : "))
ph = float(input("cobro por hora de cada trabajador: "))
empresa = 0

for i in range(1,nt+1):
    semana= int(input(f"Cuantas horas hecho el empleado {i} esta semana= "))
    sueldo = semana*ph
    empresa += sueldo
    print(f"El empleado {i} gana al mes= {sueldo}€")
    
print(f"La empresa invierte en trabajadores= {empresa}€")
    
    
    
   


