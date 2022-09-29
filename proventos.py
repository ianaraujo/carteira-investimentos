from operator import index
import os
import re
import unidecode
import sqlite3

import pandas as pd
# import numpy as np


# extratos-proventos-xxxx

files = os.listdir('./data')

proventos_files = [i for i in files if 'proventos' in i]

proventos = pd.DataFrame()

for arquivo in proventos_files:

   data = pd.read_excel(f"./data/{arquivo}", engine='openpyxl')

   proventos = pd.concat([proventos, data])


# selecionar colunas de interesse

proventos = proventos[['Produto', 'Pagamento', 'Tipo de Evento', 'Valor líquido']]


# limpeza dos nomes das colunas

def change_names(col_name):
    # 'lower case' e remove 'de' ou 'do'
    new_name = re.sub('\\b(de|do| )\\b', '_', col_name.lower())

    new_name = unidecode.unidecode(new_name.replace('___', '_'))

    return new_name

proventos = proventos.rename(columns=change_names)


# transformação dos dados

proventos['produto'] = proventos['produto'].str.extract('^(.*?)\s')

proventos.loc[proventos['tipo_evento'] == "Juros Sobre Capital Próprio", 'tipo_evento'] = 'JCP'

proventos['pagamento'] = pd.to_datetime(proventos['pagamento'], format='%d/%m/%Y').dt.date

# salva em banco de dados sqlite3

conn = sqlite3.connect('data/ct_investimentos.db')

proventos.to_sql('tb_proventos', conn, if_exists='replace', index=False)

conn.close()