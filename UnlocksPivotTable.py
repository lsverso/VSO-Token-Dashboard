import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv(r'C:\Users\L.SCHEUER\PycharmProjects\VSO-Token-Unlocks\VSO Unlocks Not Ordered 20211017.csv')
print(df.to_dict())
df['Date of Unlock'] = pd.to_datetime(df['Date of Unlock'])
pivot_table = df.pivot_table(index=['Date of Unlock', 'Internal or External'], values=['VSO Amount'], fill_value=0, aggfunc=np.sum)

pivot_table.unstack().plot(kind='bar', stacked=True)

plt.show()




# print(pivot_table.head())