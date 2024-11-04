from selenium import webdriver 
from selenium.webdriver.common.by import By

import pandas as pd

#cria um objeto para manipular o navegador
driver = webdriver.Chrome()

#abre um endereço no navegador
driver.get("https://sg.portal-pokemon.com/play/pokedex/0001")

#seleciona o elemento que possui o número do pokemon
elementNumero = driver.find_element(By.CLASS_NAME, "pokemon-slider__main-no")

#seleciona o elemento que possui o nome do pokemon
elementNome = driver.find_element(By.CLASS_NAME, "pokemon-slider__main-name")

#seleciona o elemento que possui o tipo do pokemon
elementsTipo = driver.find_elements(By.CSS_SELECTOR, ".pokemon-type a>span")

#seleciona o elemento que possui o altura do pokemon
elementAltura = driver.find_element(By.CSS_SELECTOR, ".pokemon-info__height .pokemon-info__value")

#seleciona o elemento que possui o categoria do pokemon
elementCategoria = driver.find_element(By.CSS_SELECTOR, ".pokemon-info__category .pokemon-info__value")

#seleciona o elemento que possui o peso do pokemon
elementPeso = driver.find_element(By.CSS_SELECTOR, ".pokemon-info__weight .pokemon-info__value")


print("Número: ", elementNumero.text)
print("Nome: ", elementNome.text)
print("Altura: ", elementAltura.text)
print("Categoria: ", elementCategoria.text)
print("Peso: ", elementPeso.text)
for tipo in elementsTipo:
    print("Tipo: ", tipo.text)


df = pd.DataFrame(columns=['Numero', 'Nome'])
df.loc[1] = [elementNumero.text, elementNome.text]
df.to_excel('planilha.xlsx')

import os

os.path.splitext()[1]

#impede o fechamento do navegador
input("Digite algo para terminar")