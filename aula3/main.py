from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

browser = webdriver.Chrome()

#abre um endereço no navegador
#get equivale a digitar uma url na barra de endereço do navegador
browser.get('http://www.google.com')


#procura na página um elemento que possui o ID = APjFqb
campo_pesquisa = browser.find_element(By.ID, value="APjFqb")

#digita no elemento encontrado o texto
campo_pesquisa.send_keys("como criar um robo web para ...")

#pressiona a tecla enter
#campo_pesquisa.send_keys(Keys.ENTER)

#procura o botão estou com sorte, seu nome é btnI
btn_estouComSorte = browser.find_elements(By.NAME, "btnI")

#enviar um código javascript para ser executado no navegador
#browser.execute_script('document.body.style.backgroundColor = "red";')
#titulo = browser.execute_script('return document.title;')
#print("o titulo dessa página é: ", titulo)
#browser.execute_script('arguments[0].click()', btn_estouComSorte)

btn_estouComSorte[1].click()

#impede que a página feche após executar todos os comandos
input('digite algo para fechar')