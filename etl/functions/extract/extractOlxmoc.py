from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# filtro de página &o=1

options = Options()
options.add_argument("--ignore-certificate-errors")
options.add_argument("--incognito")
options.add_argument("user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/134.0.0.0 Safari/537.36")

options.add_argument("--headless")
driver = webdriver.Chrome(options=options)

def extractOlxMoc():
    o = 1
    driver.get(f'https://www.olx.com.br/imoveis/aluguel/estado-mg/regiao-de-montes-claros-e-diamantina/montes-claros?q=apartamentos&o={o}')
    o+=1 # controla paginação do olx

    id = 1 # id do json
    anuncios = driver.find_elements(By.CSS_SELECTOR, '.olx-ad-card.olx-ad-card--horizontal')
    wait = WebDriverWait(driver, 10)
    dictEmps = {'entidades': {}}
    for anuncio in anuncios:
        titulo = anuncio.find_element(By.CSS_SELECTOR, '.olx-text.olx-text--title-small.olx-text--block.olx-ad-card__title.olx-ad-card__title--horizontal').text
        preco = wait.until(
            EC.presence_of_element_located((By.CSS_SELECTOR, '.olx-text.olx-text--body-large.olx-text--block.olx-text--semibold.olx-ad-card__price'))
        ).text
        fullEndereco = anuncio.find_element(By.CSS_SELECTOR, '.olx-ad-card__location-date-container .olx-text.olx-text--caption.olx-text--block.olx-text--regular').text
        link = wait.until(
            EC.presence_of_element_located((By.CSS_SELECTOR, '.olx-ad-card__link-wrapper'))
        ).get_attribute('href')

        dictEmps['entidades'][f'{id}'] = {
            'id': id,
            'nome': titulo,
            'preco': preco,
            'endereco': fullEndereco,
            'link': link
        }
        id+=1

    return dictEmps

        