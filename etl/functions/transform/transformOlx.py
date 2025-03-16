import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from extract.extractOlxmoc import extractOlxMoc
import pandas as pd

emps = extractOlxMoc()
# conversão de um dicionário para dataframe
def convertDictToDataframe(dictonary):
    df = pd.DataFrame.from_dict(dictonary['entidades'],orient='index')
    return df

# criando colunas cidade e bairro
def createCityAndNeighborhood():
    df = convertDictToDataframe(emps)
    df[['cidade', 'bairro']] = df['endereco'].str.split(',', expand=True)
    df = df.drop('endereco', axis=1)
    return df
