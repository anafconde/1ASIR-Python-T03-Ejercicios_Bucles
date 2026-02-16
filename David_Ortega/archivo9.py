
base = int(input("Pon un numero"))
exponente = int(input("Pon su exponente"))
resultado = base
for i in range(1, exponente):
    resultado = resultado * base

print(resultado)
