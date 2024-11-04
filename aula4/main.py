from selenium import webdriver 
from selenium.webdriver.common.by import By

import pandas as pd
import wget

#cria um objeto para manipular o navegador
driver = webdriver.Chrome()

#cria uma planilha para salvar os dados do pokemon
planilha= pd.DataFrame(columns=['Numero', 'Nome', 'Altura', 'Categoria', 'Peso', 'Tipo', 'Image'])

#cria um laço de repetição para saçlvar dados de mais pokemons
for numero in range(1, 10):
    codigoPoke = str(numero).zfill(4)

    #abre um endereço no navegador
    driver.get("https://sg.portal-pokemon.com/play/pokedex/"+codigoPoke)



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
    
    #seleciona o elemento image
    elementImage = driver.find_element(By.CLASS_NAME, "pokemon-img__front")
    urlOrigin = elementImage.get_attribute('src')
    extensao = urlOrigin.split(".")[-1]
    urlDestino = "aula4\\img\\"+codigoPoke +  "." + extensao
    #faz o donload da imagem
    wget.donload(urlOrigin, urlDestino)


    print("Número: ", elementNumero.text)
    print("Nome: ", elementNome.text)
    print("Altura: ", elementAltura.text)
    print("Categoria: ", elementCategoria.text)
    print("Peso: ", elementPeso.text)


    tipos = ""
    for tipo in elementsTipo:
        print("Tipo: ", tipo.text)
        tipos = tipo.text +  ", " + tipos


    #planilha= pd.DataFrame(columns=['Numero', 'Nome', 'Altura', 'Categoria', 'Peso', 'Tipo'])
    planilha.loc[numero-1]= [elementNumero.text, elementNome.text, elementAltura.text, elementCategoria.text, elementPeso.text, tipos, urlDestino]

planilha.to_excel('pokedex.xlsx', index = False)



#impede o fechamento do navegador
input("Digite algo para terminar")