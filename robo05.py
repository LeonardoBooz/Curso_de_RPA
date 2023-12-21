import rpa as r
import pyautogui as p
import pygetwindow as pgw
import pandas as pd

r.init()
r.url('https://rpachallengeocr.azurewebsites.net/')
maxiT = pgw.getActiveWindow().maximize()
p.sleep(7)

count_page = 1
while count_page <= 3:
    r.table('//*[@id="tableSandbox"]', 'Temp.csv')
    dados = pd.read_csv('Temp.csv')
    if count_page == 1:
        dados.to_csv('Web_table.csv', mode='a', index=None, header=True)
    else:
        dados.to_csv('Web_table.csv', mode='a', index=None, header=False)
    r.click('//*[@id="tableSandbox_next"]')
    count_page+=1
r.close()