"""
Hacer un programa que muestre un cronómetro, indicando las horas, minutos y segundos.
"""
import time, os

h=minu=sec=59
while True:
    print(f"Cronometro: {h:02d}h:{minu:02d}min:{sec:02d}s")
    time.sleep(1)
    sec+=1
    if sec==60:
        minu+=1
        sec=0
    if minu==60:
        minu=0
        h+=1
    os.system("clear")
    #os.system("cls") Este si tu Sistema Operativo es un Windows