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

# LOAD