#Ejercicio 12
#Realizar un algoritmo para determinar cuánto ahorrará una persona en un año, 
#si al final de cada mes deposita cantidades variables de dinero; además, 
#se quiere saber cuánto lleva ahorrado cada mes.
total= 0
for mes in range(1, 13):
    cant= float(input("Pon cuánto dinero ahorras en el mes" +str(mes)+ ": "))
    total= total+cant
    print("Tu ahorro total es: ", total)
print("Tu ahorro total este año es: ", total)
