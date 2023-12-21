import pyautogui as p
from time import sleep
from os import remove


# p.click(x=1453, y=640)
# p.screenshot(r'C:\Curso02\teste_foto.png', region=(403, 917, 550, 40))
# x, y = p.locateCenterOnScreen(r'C:\Curso02\teste_foto.png')
# p.click(x - 100, y, clicks = 3, duration=0.5)
# p.hotkey('ctrl', 'c')

p.click(x=1448, y=586)
texto = list(p.locateAllOnScreen(r'C:\Curso02\teste\chat_logo_2.png', confidence=0.9))[-1]
x, y = str(p.center(texto))[8:-1].split(', y=')
p.moveTo(int(x) - 20, int(y) + 20)
p.mouseDown()
p.moveTo(x=1869, y=928)
p.hotkey('ctrl', 'c')
p.mouseUp()