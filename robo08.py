import pygetwindow
from selenium.webdriver import Chrome
from time import sleep
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys


navegador = Chrome()
pygetwindow.getActiveWindow().maximize()
navegador.get('https://busca.inpi.gov.br/pePI/servlet/LoginController?action=login')
sleep(5)
navegador.find_element(By.XPATH,'//*[@id="Map3"]/area[2]').click()
sleep(2)
navegador.find_element(By.XPATH, '//*[@id="principal"]/table[2]/tbody/tr[7]/td[2]/font[1]/input').send_keys('03768202000176')
navegador.find_element(By.XPATH, '//select[2]/option[4]').click()
navegador.find_element(By.XPATH, "//input[@value=' pesquisar » ']").click()
navegador.quit()