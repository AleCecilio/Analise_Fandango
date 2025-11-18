import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt


fandango = pd.read_csv('data/fandango_scrape.csv')
all_sites = pd.read_csv('data/all_sites_scores.csv')


# Aviso: exibindo primeiras linhas
print("Primeiras linhas do dataset Fandango:")
print('-' * 75)
print(fandango.head())
print('-' * 75, '\n')


# Aviso: informações gerais
print("Informações do dataset Fandango:")
print('-' * 75)
print(fandango.info())
print('-' * 75, '\n')


# Aviso: estatísticas básicas
print("Estatísticas descritivas do Fandango:")
print('-' * 75)
print(fandango.describe())
print('-' * 75, '\n')


# Aviso: gráfico Rating vs Votes
print("Gerando gráfico: Rating vs Votes...")

plt.figure(figsize=(6.4,3.8), dpi=150)
sns.scatterplot(x='RATING', y='VOTES', data=fandango)
plt.savefig('plots/rating_vs_votes.jpg')
plt.show()

# Aviso: exibindo correlação
print("Correlação entre colunas numéricas:")
print('-' * 75)
print(fandango.select_dtypes(include='number').corr())
print('-' * 75, '\n')


# Aviso: extraindo ano do título
print("Extraindo ano do título dos filmes...")

fandango['YEAR'] = fandango['FILM'].str.extract(r'\((\d{4})\)').astype(int)
fandango['FILM'] = fandango['FILM'].str.replace(r'\s*\(\d{4}\)', '',regex=True)

print('-' * 75)
print(fandango.head())
print('-' * 75, '\n')


# Aviso: contagem por ano
print("Contagem de filmes por ano:")
print('-' * 75)
print(fandango['YEAR'].value_counts())
print('-' * 75, '\n')


# Aviso: gráfico de contagem por ano
print("Gerando gráfico: Contagem por ano...")

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


# Aviso: top 10 por votos
print("Top 10 filmes por número de votos:")
print('-' * 75)
print(fandango.nlargest(10,'VOTES'))
print('-' * 75, '\n')

# Aviso: quantidade de filmes sem votos
print("Calculando filmes sem votos...")

sem_votos = fandango['VOTES']==0
print('-' * 75)
print('Total de Filmes sem votos: ',sem_votos.sum())
print('-' * 75, '\n')


fan_reviewed = fandango[fandango['VOTES']>0].copy()


# Aviso: gerando KDE plot
print("Gerando gráfico KDE de Rating vs Stars...")

plt.figure(figsize=(6.8, 3.4), dpi=125)

sns.kdeplot(
    data=fan_reviewed,
    x='RATING',      
    fill=True,
    alpha=0.4,
    label="Stars Displayed"
)

sns.kdeplot(
    data=fan_reviewed,
    x='STARS',
    fill=True,
    alpha=0.4,
    label="True Rating"
)

plt.xlabel("RATING")
plt.ylabel("Density")
plt.xlim(0,5)
plt.legend(fontsize=8)
plt.savefig('plots/rating_vs_stars.jpg')
plt.show()


# Aviso: calculando diferença entre stars e rating
print("Calculando diferença STARS - RATING...")

fan_reviewed['STARS_DIFF'] = (
    fan_reviewed['STARS']
    - fan_reviewed['RATING']
).round(1)

print('-' * 75)
print(fan_reviewed)
print('-' * 75, '\n')


# Aviso: gráfico de contagem da diferença
print("Gerando gráfico: Contagem de STARS_DIFF...")

plt.figure(figsize=(6.8,3.4), dpi=125)

sns.countplot(
    data=fan_reviewed, 
    x='STARS_DIFF',
    hue='STARS_DIFF',
    palette='viridis',
    legend=False
)

plt.savefig('plots/stars_diff_cout.jpg')
plt.show()


# Aviso: filtrando diferença == 1
print("Filmes com diferença de 1 ponto entre Stars e Rating:")
print('-' * 75)
print(fan_reviewed[fan_reviewed['STARS_DIFF']==1])
print('-' * 75, '\n')

# Aviso: overview All Sites
print("Primeiras linhas do dataset All Sites:")
print('-' * 75)
print(all_sites.head())
print('-' * 75, '\n')

print("Colunas do All Sites:")
print('-' * 75)
print(all_sites.columns)
print('-' * 75, '\n')

print("Informações do All Sites:")
print('-' * 75)
print(all_sites.info())
print('-' * 75, '\n')

print("Estatísticas All Sites:")
print('-' * 75)
print(all_sites.describe())
print('-' * 75, '\n')


# Aviso: gráfico RottenTomatoes vs Usuarios
print("Gerando gráfico: Crítica vs Usuários...")

plt.figure(figsize=(6.8,3.4), dpi=125)
sns.scatterplot(data=all_sites,x='RottenTomatoes', y='RottenTomatoes_User')
plt.ylim(0,100)
plt.savefig('plots/RT_critic_vs_users.jpg')
plt.show()


# Aviso: calculando diferença absoluta média
print("Calculando diferença absoluta média entre crítica e usuários...")

all_sites['Rotten_Diff'] = all_sites['RottenTomatoes'] - all_sites['RottenTomatoes_User']

print('-' * 75)
print(
    'A diferença absoluta média entre crítica e usuarios é de: ',
    all_sites['Rotten_Diff'].abs().mean()
)
print('-' * 75, '\n')

