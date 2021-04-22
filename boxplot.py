import pandas as pd
import matplotlib.pyplot as plt

dados=pd.read_csv('D:/Didática_Tech/athlete_events.csv')

dados.boxplot(column=['Age','Height','Weight'])
plt.show()