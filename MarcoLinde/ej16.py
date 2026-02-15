#Ejercicio 16
#Una empresa les paga a sus empleados con base en las horas trabajadas en la semana. 
#Realice un algoritmo para determinar el sueldo semanal de N trabajadores y, 
#además, calcule cuánto pagó la empresa por los N empleados.
num= int(input("Pon el número de trabajadores: "))
pagototal= 0
pagohora= float(input("Pon a cuánto se paga la hora: "))
for i in range(num):
    horas= int(input("Horas de trabajo" +str(i+1)+ ": "))
    pago= horas*pagohora  
    print("El sueldo del trabajador", i+1, "es : ", pago)
    pagototal= pagototal+pago
print("El dinero que ha pagado la empresa en total es: ", pagototal)
