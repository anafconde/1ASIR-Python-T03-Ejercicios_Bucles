#David Ortega MArfil

lunes = int(input("Cuantas Horas trabajas el lunes?"))
martes = int(input("Cuantas Horas trabajas el martes?"))
miercoles = int(input("Cuantas Horas trabajas el miercoles?"))
jueves = int(input("Cuantas Horas trabajas el jueves?"))
viernes = int(input("Cuantas Horas trabajas el viernes?"))
total = lunes + martes + miercoles + jueves + viernes

empleado = int(input("Cuantos empleados hay?"))

print("Pago total", (total * 12) * empleado)