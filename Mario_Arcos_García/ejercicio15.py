# autor: Mario Arcos
# version: 1.0
# ejercicio 15

mensual = 10
total_pagado = 0

for mes in range(1, 21):
    print(f"Mes {mes}: {mensual} €")
    
    total_pagado = total_pagado + mensual
    
    mensual = mensual * 2

print("-" * 20)
print("Total pagado tras 20 meses:", total_pagado, "€")