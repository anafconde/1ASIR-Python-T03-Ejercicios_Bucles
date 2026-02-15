# Autor : Victor Manuel
# Version : "1.0"
# Ejercicio 14: Una persona se encuentra en el kilómetro 70 de una carretera,
# otra se encuentra en el km 150, los coches tienen sentido opuesto y tienen la misma velocidad.
# Realizar un programa para determinar en qué kilómetro de esa carretera se encontrarán.


persona1 = 70
persona2 = 150

encuentro= (persona1 - persona2) // -2 #Puse entre menos 2 para aplicar la ley de lo signos para que no salga valor negativo

for i in range(encuentro+1):
    p1= persona1 + i
    p2= persona2 - i
    
print("Ambos se cruzaran en el km=", p1)