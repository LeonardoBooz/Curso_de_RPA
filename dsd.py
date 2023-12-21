import pyautogui as p
import pandas as pd


p.hotkey('win', 'r')
p.press('backspace')
p.write('"C:\Program Files\Google\Chrome\Application\chrome.exe"')
p.press('enter')
p.sleep(3)
p.click(x=401, y=63)
p.write('http://rpachallenge.com')
p.press('enter')
p.sleep(4)


def procura(file):
    try:
        return p.center(p.locateOnScreen(file, confidence=0.9))
    except p.ImageNotFoundException:
        return False

def escreve_procura(file, content):
    x_e_y = False
    while x_e_y == False:
        x_e_y = procura(file)
        c = 0
        if c < 10:
            p.click(x=733, y=418)
            p.press('pagedown')
        else:
            p.click(x=733, y=418)
            p.press('pageup')
    x, y = x_e_y
    p.click(x, y+20)
    p.write(content)

escreve_procura(r'C:\Curso02\robo07_pyautogui\first_name.png', 'certo')