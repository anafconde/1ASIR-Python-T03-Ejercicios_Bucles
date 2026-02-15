total_ahorrado = 0
for mes in range(1, 13):
    ingreso = float(input("¿Cuánto dinero ahorras el mes " + str(mes) + "?: "))
    total_ahorrado += ingreso
    print("Llevas ahorrado:", total_ahorrado)

print("Al final del año has ahorrado:", total_ahorrado)