# Autor: Jose Rodriguez
# Versión: 1.0
# Ejercicio 12
# Realizar un algoritmo para determinar cuánto ahorrará una persona en un año, 
# si al final de cada mes deposita cantidades variables de dinero; además, se quiere saber cuánto lleva ahorrado cada mes.

ahorros = 0 
for i in range(1,13): 
    deposito=float(input(f"Cuanto depositates el mes {i}:  "))
    ahorros += deposito
    print (f"Tienes ahorrado {ahorros}€") 
print (f"Tus ahorros al final de año son {ahorros}")