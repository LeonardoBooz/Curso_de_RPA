import pyautogui as p
import pandas as pd
import pygetwindow as pgw



posicao_pagina = 1
def procura(file):
        return p.locateCenterOnScreen(file, confidence = 0.9, minSearchTime=5)

def localiza_escreve(file, content = None, writer = True):
    x, y = procura(file)
    if writer:
        p.click(x, y+20)
        p.write(content)
    else:
        p.click(x, y)


p.hotkey('win', 'r')
p.press('backspace')
p.write('"C:\Program Files\Google\Chrome\Application\chrome.exe"')
p.press('enter')
p.sleep(3)
pgw.getActiveWindow().maximize()
p.click(x=401, y=63)
p.write('http://rpachallenge.com')
p.press('enter')
p.sleep(5)

dados = pd.read_excel(r'C:\Curso02\challenge.xlsx', sheet_name='Sheet1')
df = pd.DataFrame(dados)

p.click(x=235, y=866)

for dado in df.itertuples():
    localiza_escreve(r'C:\Curso02\robo07_pyautogui\first_name.png', dado[1])
    localiza_escreve(r'C:\Curso02\robo07_pyautogui\last_name.png', dado[2])
    localiza_escreve(r'C:\Curso02\robo07_pyautogui\company_name.png', dado[3])
    localiza_escreve(r'C:\Curso02\robo07_pyautogui\role_company.png', dado[4])
    localiza_escreve(r'C:\Curso02\robo07_pyautogui\address.png', dado[5])
    localiza_escreve(r'C:\Curso02\robo07_pyautogui\email.png', dado[6])
    localiza_escreve(r'C:\Curso02\robo07_pyautogui\phone.png', str(dado[7]))
    localiza_escreve(r'C:\Curso02\robo07_pyautogui\submit.png', writer=False)
p.sleep(3)
p.screenshot('Score_pyautogui.png')

print()