#David Ortega Marfil

primo = int(input("Pon un numero"))

for i in range(2, primo):
    if primo % i == 0:
        print("No es primo")
        break
    else:
        print("Es primo")
        break
