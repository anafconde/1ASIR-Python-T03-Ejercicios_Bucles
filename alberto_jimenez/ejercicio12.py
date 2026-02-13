#Autor: Alberto Jiménez Mellado
#Version: 1.0
#Realizar un algoritmo para determinar cuánto ahorrará una persona en un año, si al final de cada mes deposita cantidades variables de dinero. 
#Además, se quiere saber cuánto lleva ahorrado cada mes.

print ("--------------IMAGIN BANK------------")

save = 0

for m in range(1, 13):
    ahorro = float(input(f"Ingrese la cantidad a depositar en el mes {m}: "))
    save += ahorro
    print(f"Ahorro acumulado hasta el mes {m}: {save}. ")

print(f"Al finalizar el año, el ahorro total es: {save}. ")

