import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from transform.transformOlx import createCityAndNeighborhood
from data.db import connDataBase

def insertOlxData(nome, preco, cidade, bairro, link):
    cnx = connDataBase()
    cursor = cnx.cursor()

    cursor.execute('INSERT INTO olx (nome, preco, cidade, bairro, link) VALUES (%s,%s, %s, %s, %s)', (nome, preco, cidade, bairro, link))

    cnx.commit()

    print(f'{nome} inserido no banco de dados, na tabela OLX')

def loadDataToDB():
    df = createCityAndNeighborhood()
    for index, value in df.iterrows():
        nome = value['nome']
        preco = value['preco']
        cidade = value['cidade']
        endereco = value['bairro']
        link = value['link']
        insertOlxData(nome, preco, cidade, endereco, link)