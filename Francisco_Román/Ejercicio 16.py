n_empleados = int(input("¿Cuántos empleados tiene la empresa?: "))
precio_hora = float(input("¿A cuánto se paga la hora?: "))
gasto_total_empresa = 0

for i in range(1, n_empleados + 1):
    print("Empleado", i)
    horas = float(input("Horas trabajadas esta semana: "))
    sueldo_semanal = horas * precio_hora
    print("Sueldo de este empleado:", sueldo_semanal)
    gasto_total_empresa += sueldo_semanal

print("La empresa pagó en total:", gasto_total_empresa)