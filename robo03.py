import pyautogui as p
from time import sleep
from datetime import datetime

hora_sistema = str(datetime.now())[:19]


p.hotkey('win', 'r')
p.press('backspace')
p.click(x=319, y=607)
p.typewrite('C:\Program Files\Google\Chrome\Application\chrome.exe')
p.click(x=157, y=672)
sleep(2)
p.click(x=471, y=68)
p.typewrite('https://www.melhorcambio.com/dolar-hoje')
p.press('enter')
sleep(2)
p.click(x=547, y=510)
p.hotkey('ctrl', 'c')
p.click(x=612, y=59)
p.typewrite('https://www.gmail.com')
p.press('enter')
sleep(4)
p.click(x=66, y=184)
sleep(3)
p.click(x=882, y=304)
sleep(3)
p.typewrite('leonardobooz345@gmail.com')
p.click(x=889, y=337)
p.typewrite(f'Cotação do dolar no dia: {hora_sistema}')
p.click(x=840, y=389)
p.hotkey('ctrl', 'v')
p.click(x=843, y=685)

