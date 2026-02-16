# autor: Mario Arcos
# version: 1.0
# ejercicio 17

num_empleados = int(input("Número de empleados: "))
precio_por_hora = float(input("Pago por hora: "))

total_de_empresa = 0

for i in range(1, num_empleados + 1):
    horas = float(input(f"Horas totales del empleado {i}: "))
    sueldo = horas * precio_por_hora
    print(f"Sueldo: {sueldo}")
    total_empresa += sueldo

print("Total pagado por la empresa:", total_empresa)