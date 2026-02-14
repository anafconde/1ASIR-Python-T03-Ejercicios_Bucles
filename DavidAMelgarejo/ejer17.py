"""
Una empresa les paga a sus empleados con base en las horas trabajadas en la semana. 
Para esto, se registran los días que trabajó y las horas de cada día.
Realice un algoritmo para determinar el sueldo semanal de N trabajadores y 
además calcule cuánto pagó la empresa por los N empleados.
"""
trabajadores={}
sueldo=9
sueldoTotal=0
while True:
    try:
        n=int(input("Numero de trabajadores: "))
        if n>0:break
        else:print("Tiene que ser al menos 1 Trabajador")
    except ValueError:
        print("Valor no valido")
for i in range(n):
    nombre=""
    while nombre=="":
        nombre=input(f"Nombre del trabajador {i+1}: ").strip()
    dias={
    "Lunes": 0,
    "Martes":0,
    "Miercoles":0,
    "Jueves":0,
    "Viernes":0,
    "Sabado":0,
    "Domingo":0
    }
    for j in dias:
        while True:
            try:
                dias[j]=int(input(f"Horas que ha trabajado {nombre} el dia {j}: "))
                if dias[j]<0:print("Las horas no pueden ser < 0")
                else:break
            except ValueError:
                print("Numero no valido")
    trabajadores[nombre]=dias       

for i in trabajadores:
    horas=sum(trabajadores[i].values())
    print(f"El trabajador {i} ha trabajado {horas} horas")
    print(f"Su sueldo semanal es: {horas*sueldo}€")
    sueldoTotal+=horas*sueldo
print(f"La empresa ha gastado {sueldoTotal}€ en salarios")

