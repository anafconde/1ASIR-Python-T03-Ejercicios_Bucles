"""
Una empresa tiene el registro de las horas que trabaja diariamente un empleado durante la semana
(seis días) y requiere determinar el total de éstas, así como el sueldo que recibirá por las horas trabajadas.
"""
horas=[7,6,8,7,8,9]
d_hora=9
print(f"Ha trabajado {sum(horas)} horas.\n A {d_hora}€/h el sueldo de la semana es: {d_hora*sum(horas)}€")