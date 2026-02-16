# autor: Mario Arcos
# version: 1.0
# ejercicio 5

print("Introduce caracteres:")

while True:
    carac = input("Introduce un carácter: ")

    if carac == " ":
        print("El programa ha finalizado.")
        break
    
    if carac.lower() in "aeiou":
        print("VOCAL")
    else:
        print("NO VOCAL")