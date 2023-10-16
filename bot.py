import time
import pyautogui

"""time.sleep(5)
var = open("archivo.txt","r")
for linea in var:
    pyautogui.typewrite(linea)
    pyautogui.press('enter')
"""
time.sleep(5)

for i in range(20):
    pyautogui.typewrite("hola amigue")
    pyautogui.press('enter')