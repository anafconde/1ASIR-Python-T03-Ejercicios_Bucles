"""
Realizar un algoritmo para determinar cuánto ahorrará una persona en un año, 
si al final de cada mes deposita cantidades variables de dinero. Además, se quiere saber cuánto lleva ahorrado cada mes.
"""
ahorrado=mes=0
meses=["Enero","Febrero","Marzo","Abril","Mayo","Junio","Julio","Agosto","Septiembre","Octubre","Noviembre","Diciembre"]
while mes<12:
    try:
        depos=float(input("Cuanto quieres depositar: "))
        ahorrado+=depos
        print(f"En {meses[mes]} llevas ahorrado: {ahorrado}€")
        mes+=1
    except ValueError:
        print("No es un valor valido")
else:
    print(f"En todo este año has ahorrado: {ahorrado}€")