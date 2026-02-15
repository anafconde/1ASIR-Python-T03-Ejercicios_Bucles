# Autora: Noelia López Poyatos
# Version: 1.0
# Descripción: Primeros pasos con Python
# Fecha: 2025-02-13

# Ejercicio 12: Ahorro mensual. 
# Realizar un algoritmo para determinar cuánto ahorrará una persona en un año, si al final de cada mes deposita cantidades variables de dinero. 
# Además, se quiere saber cuánto lleva ahorrado cada mes.

# Ahorro mensual

mes = 1       
total_ahorrado = 0  

while mes <= 12:  
    deposito = float(input("Introduce cuánto ahorras en el mes " + str(mes) + ": "))
    total_ahorrado = total_ahorrado + deposito  
    
    print("Llevas ahorrado:", total_ahorrado, "euros")
    
    mes = mes + 1  

print("En total, has ahorrado:", total_ahorrado, "euros en un año")
