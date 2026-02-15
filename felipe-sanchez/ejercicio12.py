# Autor: Felipe
# Version: 1.0
# Ejercicio 12
# Realizar un algoritmo para determinar cuánto ahorrará una persona en un año,
# si al final de cada mes deposita cantidades variables de dinero; además, se quiere saber cuánto lleva ahorrado cada mes.



total=0

while True:
    mes=int(input("Introduzca el numero del mes o intruduzca 0 para salir: "))    
    
    if mes == 0:
        break
    
    if 0 < mes < 13:
        dinero=float(input("¿Cuanto dinero ahorraras este mes: "))
        total+=dinero
        print("Con lo ingresado este mes llevas un total de :",total,"€")
    else:
        print("Numero de mes introducido incorrecto")


print("En todo el año llevas ahorrado: ",total,"€")