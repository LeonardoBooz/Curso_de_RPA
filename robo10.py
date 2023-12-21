import pygetwindow
from selenium.webdriver import Chrome
from time import sleep
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys


cnpjs = ["45997418000153", "72273196001090", "33000167000101"]

nav = Chrome()
pygetwindow.getActiveWindow().maximize()
nav.get('https://consultacnpj.com/cnpj/')
nav.find_element(By.XPATH, '//*[@id="modal"]/div/div[2]/div/div[2]/a[1]').click()
for cnpj in cnpjs:
    nav.find_element(By.XPATH, '//*[@id="__layout"]/div/div[2]/div/div[2]/div/div/div[1]/div[2]/div/div/input').clear()
    nav.find_element(By.XPATH, '//*[@id="__layout"]/div/div[2]/div/div[2]/div/div/div[1]/div[2]/div/div/input').send_keys(cnpj)
    sleep(5)
    dados = nav.find_element(By.XPATH, '//*[@id="company-data"]')
    with open('dados_empresariais.txt', 'a') as arq:
        arq.write(dados.text)



