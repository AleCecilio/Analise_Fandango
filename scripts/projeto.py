import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

fandango = pd.read_csv('data/fandango_scrape.csv')

print('-' * 55)
print(fandango.head())
print('-' * 55, '\n')

print('-' * 55)
print(fandango.info())
print('-' * 55, '\n')

print('-' * 55)
print(fandango.describe())
print('-' * 55, '\n')

plt.figure(figsize=(6.4,3.8), dpi=150)
sns.scatterplot(x='RATING', y='VOTES', data=fandango)
plt.savefig('plots/rating_vs_votes.jpg')
plt.show()

print('-' * 55)
print(fandango.select_dtypes(include='number').corr())
print('-' * 55, '\n')


fandango['YEAR'] = fandango['FILM'].str.extract(r'\((\d{4})\)').astype(int)
fandango['FILM'] = fandango['FILM'].str.replace(r'\s*\(\d{4}\)', '', regex=True)
print('-' * 55)
print(fandango.head())
print('-' * 55, '\n')


print('-' * 55)
print(fandango['YEAR'].value_counts())
print('-' * 55, '\n')


plt.figure(dpi=125)
sns.countplot(
    data=fandango, 
    x='YEAR',
    order=[2015,2014,2016,1964,2012],
    hue='YEAR',
    palette='Set1',
    legend=False
)
plt.gca().spines['bottom'].set_linewidth(0.2)

plt.ylim(bottom=0)
plt.savefig('plots/contagem_por_ano.jpg')
plt.show()


print('-' * 55)
print(fandango.nlargest(10,'VOTES'))
print('-' * 55, '\n')


sem_votos = fandango['VOTES']==0
print('-' * 55)
print('Total de Filmes sem votos: ',sem_votos.sum())
print('-' * 55, '\n')

fan_reviewed = fandango[fandango['VOTES'>0]]