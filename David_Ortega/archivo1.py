#David Ortega MArfil

factorial = int(input("Pon un numero"))
resultado = 1
for i in range(1, factorial + 1):
    resultado = i * resultado
    
print(resultado)