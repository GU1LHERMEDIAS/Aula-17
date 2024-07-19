# import seaborn as sns
import openpyxl
import pandas as pd
# import matplotlib.pyplot as 
import numpy as np

data = ({'colunas':['a','b','c','d'],
          'x':[1,3,5,6],
          'y':[56,8,9,7]})
df = pd.DataFrame(data)
caminho = 'dados5.xlsx'
caminho2 = 'dados7.xlsx'
caminho3 = 'dados8.xlsx'

for n in range(1,4):
    df.to_excel(caminho, index=False)
    df.to_excel(caminho2, index=False)
    df.to_excel(caminho3, index=False)