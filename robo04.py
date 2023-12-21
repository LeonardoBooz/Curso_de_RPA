import pyautogui as p
import pygetwindow as pgw


p.hotkey('win', 'r')
p.press('backspace')
p.click(x=319, y=607)
p.typewrite('C:\Program Files\Google\Chrome\Application\chrome.exe')
p.click(x=157, y=672)
p.sleep(4)
pgw.getActiveWindow().maximize()
p.click(x=471, y=68)
p.typewrite('https://www.udemy.com')
p.press('enter')
p.sleep(4)
local_pesq = p.locateOnScreen('Captura de tela 2023-12-19 085749.PNG', confidence=0.9)
local_pesquisa = p.center(local_pesq)
x, y = local_pesquisa
p.click(x, y)
p.write('cursos de python')
p.press('enter')
p.sleep(4)
p.screenshot('Cursos.png')
p.sleep(4)
local_pesq = p.locateOnScreen('Captura de tela 2023-12-19 085914.png', confidence=0.9)
local_pesquisa = p.center(local_pesq)
x, y = local_pesquisa
p.click(x, y)


