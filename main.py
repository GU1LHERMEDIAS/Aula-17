import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt

df = pd.DataFrame('x',[1,2,3],'y',[4,5,6])

sns.implot(data=df,x='x',y='y')#seaborn
plt.plot(df)#matplotlib

plt.show()
