import pyautogui as pg 
import time
import os

# Esperar unos segundos para prepararse
time.sleep(2)


# Abrir el Bloc de notas (en Windows)


pg.hotkey('win', 'r')

time.sleep(1)


# Escribir un mensaje
pg.write("RDP", interval=0.05)
captura =pg.screenshot()
captura.save("C:/Users/2909287/Pictures/Evidencia eventos/Julio 2025/mi_imagen.png")


# Simular presionar Enter y escribir otra línea
pg.press("enter")


