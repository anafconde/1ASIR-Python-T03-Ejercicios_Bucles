# Autor : Victor Manuel
# Version : "1.0"
# Ejercicio 12: 
# Realizar un algoritmo para determinar cuánto ahorrará una persona en un año, 
# si al final de cada mes deposita cantidades variables de dinero; además, 
# se quiere saber cuánto lleva ahorrado cada mes.

ahorros = 0 #contador de ahorros
for i in range(1,12+1): # bucle de Meses 
    deposito=float(input(f"Cuanto depositates el mes de {i}= "))
    ahorros += deposito
    print (f"llevas ahorrado= {ahorros}€") # Dinero acumulado en el contador
    
print (f"ahorraste al final de año= ${ahorros}") # Dinero acumulado en el contador