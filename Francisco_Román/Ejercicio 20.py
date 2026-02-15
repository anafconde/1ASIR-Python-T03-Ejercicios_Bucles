cantidad_objetivo = int(input("¿Cuántos números primos quieres mostrar?: "))
encontrados = 0
numero_actual = 2

while encontrados < cantidad_objetivo:
    es_primo = True
    
    for i in range(2, numero_actual):
        if numero_actual % i == 0:
            es_primo = False
            break
    
    if es_primo:
        print(numero_actual)
        encontrados += 1
    
    numero_actual += 1