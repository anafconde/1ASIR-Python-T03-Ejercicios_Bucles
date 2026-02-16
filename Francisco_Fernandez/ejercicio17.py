# Autor: Paco Fernandez
# Version: 1.0
# Una empresa les paga a sus empleados con base en las horas trabajadas en la semana. 
# Para esto, se registran los días que trabajó y las horas de cada día. 
# Realice un algoritmo para determinar el sueldo semanal de N trabajadores y además 
# calcule cuánto pagó la empresa por los N empleados.

trabajadores = int(input("Ingrese el número de trabajadores: "))
total = 0  

for trabajador in range(1, trabajadores + 1):
    print(f"Trabajador {trabajador}")
    dias = int(input("Ingrese el número de días trabajados esta semana: "))
    horas = 0  
    
    for dia in range(1, dias + 1):
        horas += float(input(f"Horas trabajadas el día {dia}: "))
    
    precio_hora = float(input("Ingrese el pago por hora: "))
    sueldo = horas * precio_hora
    print(f"Sueldo semanal del trabajador {trabajador}: {sueldo} €")
    
    total = total + sueldo  

print(f"Total pagado por la empresa a los {trabajadores} trabajadores: {total} €")
