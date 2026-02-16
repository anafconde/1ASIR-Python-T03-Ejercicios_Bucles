# autor: Mario Arcos
# version: 1.0
# ejercicio 11

n = int(input("Introduce un número: "))
es_primo = True

if n < 2:
    es_primo = False
else:
    for i in range(2, n):
        if n % i == 0:
            es_primo = False
            break

if es_primo:
    print("El número es PRIMO")
else:
    print("El número no es PRIMO")
