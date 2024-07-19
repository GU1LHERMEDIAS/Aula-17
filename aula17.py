import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_excel('BASE.xlsx')
sns.barplot(data = df, x='vendedor', y='vendas')

plt.show()