from selenium.webdriver import Chrome
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from time import sleep
import pandas as pd


nav = Chrome()
nav.get('http://rpachallenge.com')
nav.fullscreen_window()

dados = pd.read_excel(r'C:\Curso02\challenge.xlsx', sheet_name='Sheet1')

df = pd.DataFrame(dados)
sleep(5)
nav.find_element(By.XPATH, '/html/body/app-root/div[2]/app-rpa1/div/div[1]/div[6]/button').click()
for dado in df.itertuples():
    nav.find_element(By.XPATH, '//*[@ng-reflect-name="labelFirstName"]').send_keys(dado[1])
    nav.find_element(By.XPATH, '//*[@ng-reflect-name="labelLastName"]').send_keys(dado[2])
    nav.find_element(By.XPATH, '//*[@ng-reflect-name="labelCompanyName"]').send_keys(dado[3])
    nav.find_element(By.XPATH, '//*[@ng-reflect-name="labelRole"]').send_keys(dado[4])
    nav.find_element(By.XPATH, '//*[@ng-reflect-name="labelAddress"]').send_keys(dado[5])
    nav.find_element(By.XPATH, '//*[@ng-reflect-name="labelEmail"]').send_keys(dado[6])
    nav.find_element(By.XPATH, '//*[@ng-reflect-name="labelPhone"]').send_keys(dado[7])
    nav.find_element(By.XPATH, '/html/body/app-root/div[2]/app-rpa1/div/div[2]/form/input').click()
sleep(3)
nav.save_screenshot('Score_Selenium.png')
nav.quit()
