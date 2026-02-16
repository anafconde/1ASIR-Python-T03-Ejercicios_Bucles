# Autor: Paco Fernandez
# Version: 1.0
# Algoritmo que pida números hasta que se introduzca un cero. 
# Debe imprimir la suma y la media de todos los números introducidos.
    
numero = 1
suma = 0 
contador = 0

while numero != 0:
    numero = int(input("Introduce un numero (0 para terminar): "))

    if numero != 0:
        suma += numero
        contador = contador + 1
    
media = suma / contador
print(f"La suma de los numeros introducidos es {suma}")
print(f"La media de los numeros introduidos es {media}")