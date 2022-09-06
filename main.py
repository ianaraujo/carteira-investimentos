import os
import re
import warnings
import unidecode
import sqlite3
import pandas as pd

warnings.simplefilter('ignore')

# EXTRACT

files = os.listdir('./data')

negociacao_files = [i for i in files if 'negociacao' in i]

df = pd.DataFrame()

for arquivo in negociacao_files:

   data = pd.read_excel(f"./data/{arquivo}")

   df = pd.concat([df, data]) 

df_subscricoes = pd.read_csv('./data/extrato_subscricoes.csv')

# TRANSFORM 

df = df.drop(['Mercado', 'Prazo/Vencimento', 'Instituição', 'Valor'], axis=1)

def change_names(col_name):
   new_name = re.sub('\\b(de|do)\\b', '_', col_name.lower())
   new_name = unidecode.unidecode(new_name.replace(' ', ''))

   return new_name

df = df.rename(columns=change_names)

df = pd.concat([df, df_subscricoes], ignore_index=True)

df['data_negocio'] = pd.to_datetime(df['data_negocio'], format='%d/%m/%Y')

df['codigo_negociacao'] = df['codigo_negociacao'].str.replace(pat='F$', repl='')

df.loc[df['codigo_negociacao'] == 'TIET11', 'codigo_negociacao'] = 'AESB3'

df['tipo_movimentacao'] = df['tipo_movimentacao'].str.lower()

df.info()

# LOAD

conn = sqlite3.connect('./data/ct_investimentos.db')

df.to_sql('tb_negociacoes', conn, index=False, if_exists='replace')

conn.close()
