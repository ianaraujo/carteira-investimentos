import pandas as pd
import os

import warnings
warnings.simplefilter('ignore')

# EXTRACT

files = os.listdir('./data')

negociacao_files = [i for i in files if 'negociacao' in i]

df = pd.DataFrame()

for arquivo in negociacao_files:

   temp = pd.read_excel(f"./data/{arquivo}")

   df = pd.concat([df, temp]) 

# TRANSFORM 

df = df.iloc[:, [0, 1, 5, 6, 7]]

c_names = {'Data do Negócio':'data', 'Tipo de Movimentação':'tipo', 'Código de Negociação':'codigo', 'Quantidade':'quantidade', 'Preço':'valor'}

df.rename(columns=c_names, inplace=True)

df['codigo'] = df['codigo'].str.replace(pat='F$', repl='')

df['tipo'] = df['tipo'].str.casefold()

# LOAD