import pygetwindow
from selenium.webdriver import Chrome
from time import sleep
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

nav = Chrome()
pygetwindow.getActiveWindow().maximize()
nav.get('https://ferendum.com/pt/')
nav.find_element(By.NAME, 'titulo').send_keys('A automação é uma coisa boa?(Leonardo')
nav.find_element(By.NAME, 'descripcion').send_keys('Os robôs estão cada vez mais frequentes em nossas vidas..')
nav.find_element(By.NAME, 'creador').send_keys('Leonardo Curso RPA com Python')
nav.find_element(By.XPATH, '//input[@type="email"]').send_keys('leonardobooz99@gmail.com')
nav.find_element(By.ID, 'op1').send_keys('Sim! Ela me ajuda muito..')
nav.find_element(By.ID, 'op2').send_keys('Não! Estou com medo de perder o emprego..')
nav.find_element(By.NAME, 'config_un_solo_voto').click()
nav.find_element(By.NAME, 'accept_terms_checkbox').click()
nav.find_element(By.XPATH, '//input[@value="Criar enquete"]').click()
sleep(5)
nav.find_element(By.XPATH, '//*[@id="crear_votacion"]').click()

print()
nav.quit()