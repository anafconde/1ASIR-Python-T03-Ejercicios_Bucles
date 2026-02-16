# autor: Mario Arcos
# version: 1.0
# ejercicio 13

pago_por_hora = float(input("¿Cuánto gana el empleado por hora?: "))

total_de_horas = 0

for dia in range(1, 7):
    horas_de_dia = float(input(f"Horas trabajadas el día {dia}: "))
    total_de_horas = total_de_horas + horas_de_dia

sueldo = total_de_horas * pago_por_hora

print("\n--- Resultados ---")
print("Total de horas trabajadas:", total_de_horas)
print("Sueldo total a recibir: $", sueldo)
