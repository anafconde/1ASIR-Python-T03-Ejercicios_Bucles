# Autor: David González Mora
# versión: 1.0
# Ejercicio 12 Relación de ejercicios
# Realizar un algoritmo para determinar cuánto ahorrará una persona en un año, si al final de cada mes deposita cantidades variables de dinero; además, se quiere saber cuánto lleva ahorrado cada mes.

total = 0

for mes in range(1, 13):   
    deposito = float(input("Dinero ahorrado en el mes " + str(mes) + ": "))
    total = total + deposito
    print("Total ahorrado hasta el mes", mes, ":", total)

print("Ahorro total en el año:", total)
