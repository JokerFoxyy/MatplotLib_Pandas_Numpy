import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

dados = pd.read_csv('D:/Didática_Tech/athlete_events.csv')

dados02=dados.dropna() #exclui linhas que contém Nan

print(dados.shape)
print(dados02.shape)

enulo= dados.isnull() # onde é null fica True e onde não é fica False

faltantes= dados.isnull().sum() # Soma quantos True tem

faltantes_percentual= (dados.isnull().sum()/len(dados['ID']))*100

print(faltantes_percentual)
print('***'*30)

dados['Medal'] = dados['Medal'].fillna('Nenhuma')
dados['Age'] = dados['Age'].fillna(dados['Age'].mean())
dados['Height'] = dados['Height'].fillna(dados['Height'].mean())
dados['Weight'] = dados['Weight'].fillna(dados['Weight'].mean())

faltantes_percentual_limpo = (dados.isnull().sum()/len(dados['ID']))*100

print(dados)

print('***'*30)

print(faltantes_percentual_limpo)