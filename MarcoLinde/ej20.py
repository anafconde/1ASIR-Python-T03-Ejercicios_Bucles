#Ejercicio 20
#Mostrar en pantalla los N primero número primos. Se pide por teclado la 
#cantidad de números primos que queremos mostrar.
cant= int(input("Pon la cantidad de números primos que quieres mostrar: "))
cont= 0
num= 2
while cont<cant:
    primo= True
    div= 2
    while div<num:
        if num %div==0:
            primo= False
        div= div+1
    if primo:
        print(num)
        cont= cont+1
    num= num+1
