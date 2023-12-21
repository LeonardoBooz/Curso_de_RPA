import rpa as r
from time import sleep
import pyautogui as p
from os import remove
import pandas

def pega_mensagem():
    #p.click(x=1453, y=640)
    p.screenshot(r'C:\Curso02\teste_foto.png', region=(403, 917, 550, 40))
    x, y = p.locateCenterOnScreen(r'C:\Curso02\teste_foto.png')
    p.click(x - 200, y, clicks = 3, duration=0.5)
    p.hotkey('ctrl', 'c')
    remove(r'C:\Curso02\teste_foto.png')

def procura_texto_bot():
    p.click(x=1448, y=586)
    texto = list(p.locateAllOnScreen(r'C:\Curso02\teste\chat_logo_2.png', confidence=0.9))[-1]
    x, y = str(p.center(texto))[8:-1].split(', y=')
    p.moveTo(int(x) - 20, int(y) + 20)
    p.mouseDown()
    p.moveTo(x=1869, y=928)
    p.hotkey('ctrl', 'c')
    p.mouseUp()


bolinha_verde = 'l7jjieqr cfzgl7ar ei5e7seu h0viaqh7 tpmajp1w c0uhu3dl riy2oczp dsh4tgtl sy6s5v3r gz7w46tb lyutrhe2 qfejxiq4 fewfhwl7 ovhn1urg ap18qm3b ikwl5qvt j90th5db aumms1qt'
r.init(visual_automation=True)
p.hotkey('win', 'left')
r.url(r'https://web.whatsapp.com/')
sleep(5)
while True:
    sleep(2)
    if r.present(bolinha_verde):
        r.dclick(bolinha_verde)
        pega_mensagem()
        sleep(2)
        p.click(x=1400, y=973)
        p.hotkey('ctrl', 'v')
        p.press('enter')
        sleep(15)
        procura_texto_bot()
        p.click(x=603, y=994)
        p.hotkey('ctrl', 'v')
        p.press('enter')
        sleep(3)
        p.click(x=179, y=614)
        
    
    
