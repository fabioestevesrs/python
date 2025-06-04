"""test"""
import os
import time
from dotenv import load_dotenv
from selenium import webdriver

load_dotenv()

URL = os.getenv('URL')
NUMERO_FOLHA = os.getenv('NUMERO_FOLHA')
SENHA = os.getenv('SENHA')

navegador = webdriver.Chrome()
navegador.get(URL)
navegador.maximize_window()

time.sleep(3)

navegador.find_element('id', 'login-numero-folha').send_keys(NUMERO_FOLHA)
navegador.find_element('id', 'login-senha').send_keys(SENHA)

botao_entrar = navegador.find_element('id', 'login-entrar')
botao_entrar.click()

time.sleep(5)
