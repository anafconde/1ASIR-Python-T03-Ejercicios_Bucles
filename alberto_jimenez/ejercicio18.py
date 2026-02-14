#Autor: Alberto Jiménez Mellado
#Version: 1.0
#Hacer un programa que muestre un cronómetro, indicando las horas, minutos y segundos.

import time

h = 0
m = 0
s = 0

print ("----------------CRONÓMETRO----------------")

while True:
    print(f"{h:02d}:{m:02d}:{s:02d}")
    time.sleep(1)
    
    s += 1
    
    if s == 60:
        s = 0
        m += 1
        
    if m == 60:
        m = 0
        h += 1