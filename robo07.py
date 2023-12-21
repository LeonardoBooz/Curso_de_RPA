import rpa as r
import pyautogui as p
import pandas as pd
import pygetwindow as pgw


r.init()
maxiT = pgw.getActiveWindow().maximize()
r.url('http://rpachallenge.com')
p.sleep(7)

dados = pd.read_excel(r'C:\Curso02\challenge.xlsx', sheet_name='Sheet1')

df = pd.DataFrame(dados)

r.click('/html/body/app-root/div[2]/app-rpa1/div/div[1]/div[6]/button')
for row in df.itertuples():
    r.type('//*[@ng-reflect-name="labelFirstName"]', str(row[1]))
    r.type('//*[@ng-reflect-name="labelLastName"]', str(row[2]))
    r.type('//*[@ng-reflect-name="labelCompanyName"]', str(row[3]))
    r.type('//*[@ng-reflect-name="labelRole"]', str(row[4]))
    r.type('//*[@ng-reflect-name="labelAddress"]', str(row[5]))
    r.type('//*[@ng-reflect-name="labelEmail"]', str(row[6]))
    r.type('//*[@ng-reflect-name="labelPhone"]', str(row[7]))
    r.click('/html/body/app-root/div[2]/app-rpa1/div/div[2]/form/input')
p.sleep(5)
p.screenshot('score.png')
r.close()