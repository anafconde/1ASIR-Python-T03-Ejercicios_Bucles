# Autor: Jose Rodriguez
# Versión: 1.0
# Ejercicio 14
# Una persona se encuentra en el kilómetro 70 de una carretera, otra se encuentra en el km 150, 
# los coches tienen sentido opuesto y tienen la misma velocidad. Realizar un programa para determinar en qué 
# kilómetro de esa carretera se encontrarán.

persona =  70
other = 150

cruce =  (persona + other) // 2

print("Ambos coches tienen la misma velocidad y van en sentidos opuestos.")
print("Una persona está en el km", persona, "y la otra en el km", other)
print("Por lo tanto, se encontrarán en el km", cruce)