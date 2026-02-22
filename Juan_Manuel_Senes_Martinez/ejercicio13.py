#Una empresa tiene el registro de las horas que trabaja diariamente un empleado durante la semana (seis días) y requiere determinar el total de éstas, así como el sueldo que recibirá por las horas trabajadas.

empleado=input("introduce el nombre del empleado")
horas=0
for n in range(1,7):
    horas=horas+int(input("introduce las horas trabajadas el dia "+str(n)))
sueldo=horas*10
print("el empleado", empleado, "ha trabajado un total de", horas, "horas y su sueldo es de", sueldo, "euros")

