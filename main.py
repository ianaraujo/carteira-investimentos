import os
import warnings
import pandas as pd

warnings.simplefilter('ignore')

# EXTRACT

files = os.listdir('./data')

negociacao_files = [i for i in files if 'negociacao' in i]

df = pd.DataFrame()

for arquivo in negociacao_files:

   data = pd.read_excel(f"./data/{arquivo}")

   df = pd.concat([df, data]) 

# TRANSFORM 

df = df.drop(['Mercado', 'Prazo/Vencimento', 'Instituição', 'Valor'], axis=1)

c_names = {'Data do Negócio':'data', 'Tipo de Movimentação':'tipo', 'Código de Negociação':'codigo', 'Quantidade':'quantidade', 'Preço':'preço'}

df.rename(columns=c_names, inplace=True)

df['codigo'] = df['codigo'].str.replace(pat='F$', repl='')

# Change TIET11 for AESB3

df['tipo'] = df['tipo'].str.lower()

df['valor_operacao'] = df['quantidade'] * df['preço']



# LOAD

print(df)
