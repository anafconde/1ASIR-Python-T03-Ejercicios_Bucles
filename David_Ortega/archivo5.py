#David Ortega Marfil

caracter = input("Pon un caracter")

while caracter != " ":
    if caracter == "a" or caracter == "e" or caracter == "i" or caracter == "o" or caracter == "u":
        print("Es una vocal")
    else:
        print("No es una vocal")

if caracter == " ":
    exit()
