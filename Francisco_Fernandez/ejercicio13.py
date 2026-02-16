# Autor: Paco Fernandez
# Version: 1.0
# Una empresa tiene el registro de las horas que trabaja diariamente un empleado durante la semana 
# (seis días) y requiere determinar el total de éstas, así como el sueldo que recibirá por las 
# horas trabajadas.

horas_totales = 0

for dia in range(6):
    horas = float(input(f"Horas trabajadas del día {dia + 1}: "))
    horas_totales = horas_totales + horas

precio_hora = float(input("Pago por hora: "))

sueldo = horas_totales * precio_hora

print(f"Total de horas trabajadas: {horas_totales}")
print(f"Sueldo a recibir: {sueldo}")

