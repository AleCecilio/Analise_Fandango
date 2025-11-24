import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt


fandango = pd.read_csv('data/fandango_scrape.csv')
all_sites = pd.read_csv('data/all_sites_scores.csv')


# Exibindo primeiras linhas
print("Primeiras linhas do dataset Fandango:")
print('-' * 75)
print(fandango.head())
print('-' * 75, '\n')


# Informações gerais
print("Informações do dataset Fandango:")
print('-' * 75)
print(fandango.info())
print('-' * 75, '\n')


# Estatísticas básicas
print("Estatísticas descritivas do Fandango:")
print('-' * 75)
print(fandango.describe())
print('-' * 75, '\n')


# Gráfico Rating vs Votes
print("Gerando gráfico: Rating vs Votes...")
print('-' * 75, '\n')

plt.figure(figsize=(6.4,3.8), dpi=150)
sns.scatterplot(x='RATING', y='VOTES', data=fandango)
plt.savefig('plots/rating_vs_votes.jpg')
plt.show()

# Exibindo correlação
print("Correlação entre colunas numéricas:")
print('-' * 75)
print(fandango.select_dtypes(include='number').corr())
print('-' * 75, '\n')


# Extraindo ano do título
print('Extraindo ano do título...')
fandango['YEAR'] = fandango['FILM'].str.extract(r'\((\d{4})\)').astype(int)

print('-' * 75)
print(fandango.head())
print('-' * 75, '\n')


# Contagem por ano
print("Contagem de filmes por ano:")
print('-' * 75)
print(fandango['YEAR'].value_counts())
print('-' * 75, '\n')


# Gráfico de contagem por ano
print("Gerando gráfico: Contagem por ano...\n")
print('-' * 75, '\n')

plt.figure(dpi=150)
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


# Top 10 por votos
print("Top 10 filmes por número de votos:")
print('-' * 75)
print(fandango.nlargest(10,'VOTES'))
print('-' * 75, '\n')


# Quantidade de filmes sem votos
print('Quantidade de filmes sem votos...')
sem_votos = fandango['VOTES']==0
print('-' * 75)
print('Total de Filmes sem votos: ',sem_votos.sum())
print('-' * 75, '\n')


fan_reviewed = fandango[fandango['VOTES']>0].copy()


# Gerando KDE plot
print("Gerando gráfico KDE de Rating vs Stars...\n")
print('-' * 75, '\n')

plt.figure(figsize=(6.8, 3.4), dpi=150)

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


# Calculando diferença entre stars e rating
print("Calculando diferença STARS - RATING...")

fan_reviewed['STARS_DIFF'] = (
    fan_reviewed['STARS']
    - fan_reviewed['RATING']
).round(1)


print('-' * 75)
print(fan_reviewed)
print('-' * 75, '\n')


# Gráfico de contagem da diferença
print("Gerando gráfico: Contagem de STARS_DIFF...\n")
print('-' * 75, '\n')

plt.figure(figsize=(6.8,3.4), dpi=150)

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

# Overview All Sites
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


# Gráfico RottenTomatoes vs Usuarios
print("Gerando gráfico RottenTomatoes: Crítica vs Usuários...\n")
print('-' * 75, '\n')

plt.figure(figsize=(6.8,3.4), dpi=150)
sns.scatterplot(data=all_sites,x='RottenTomatoes', y='RottenTomatoes_User')
plt.ylim(0,100)
plt.savefig('plots/RT_critic_vs_users.jpg')
plt.show()


# Calculando diferença absoluta média
print("Calculando diferença absoluta média entre crítica e usuários...")
print('-' * 75, '\n')

all_sites['Rotten_Diff'] = all_sites['RottenTomatoes'] - all_sites['RottenTomatoes_User']

print('-' * 75)
print(
    'A diferença absoluta média entre crítica e usuarios é de: ',
    all_sites['Rotten_Diff'].abs().mean()
)
print('-' * 75, '\n')


# Gráfico de Distribição de Rotten_Diff
print('Gerando gráfico: Distribição de Rotten_Diff...\n')
print('-' * 75, '\n')

plt.figure(figsize=(6.8,3.4), dpi=150)

sns.histplot(
    data=all_sites,
    x='Rotten_Diff',
    bins=25,
    kde=True,
    alpha=0.4
)

plt.title('RT Critics Score minus RT User Score')
plt.savefig('plots/RT_critics_minus_RT_users.jpg')
plt.show()


# Gráfico de Distribição Absoluta de Rotten_Diff
print('Gerando gráfico: Distribição Absoluta de Rotten_Diff...\n')
print('-' * 75, '\n')

plt.figure(figsize=(6.8,3.4), dpi=150)

Abs_RT_Diff = all_sites['Rotten_Diff'].abs()

sns.histplot(
    data=Abs_RT_Diff,
    bins=25,
    kde=True,
    alpha=0.4
)

plt.title('Abs Diference between RT Critics Score and RT User Score')
plt.savefig('plots/abs_RT_critics_minus_RT_users.jpg')
plt.show()


# 5 Filmes com A Maior Diferença entre RT Critcs e RT Users
print('Top 5 Filmes com A Maior Diferença entre RT Critcs e RT Users')
print('-' * 75)
print(all_sites.nsmallest(5,'Rotten_Diff'))
print('-' * 75, '\n')


# 5 filmes em que a nota da crítica fica, em média, muito acima da nota dos usuários.
print(
    'Top 5 filmes em que a nota da crítica fica,' \
    ' em média, muito acima da nota dos usuários.'
)
print('-' * 75)
print(all_sites.nlargest(5,'Rotten_Diff'))
print('-' * 75, '\n')


# Gráfico de Distribuição Metacritic vs MetaCritc User
print("Gerando gráfico Metacritic: Crítica vs Usuários...\n")
print('-' * 75, '\n')

plt.figure(figsize=(6.8,3.4), dpi=150)
sns.scatterplot(data=all_sites,x='Metacritic', y='Metacritic_User')
plt.xlim(0,100)
plt.ylim(0,10)  
plt.savefig('plots/MC_critic_vs_users.jpg')
plt.show()


# Gráfico de Distribuição Contagem de Votos IMDB vs MetaCritc
print("Gerando gráfico Contagem de Votos: IMDB vs MetaCritc...\n")
print('-' * 75, '\n')

plt.figure(figsize=(6.8,3.4), dpi=150)
sns.scatterplot(
    data=all_sites,
    x='Metacritic_user_vote_count', 
    y='IMDB_user_vote_count'
) 
plt.savefig('plots/user_vote_count_Metacritic_vs_IMDB.jpg')
plt.show()


# O Filme com a maior quantidade de votos no IMDB
print("Filme com mais votos no IMDB\n")
print('-' * 75)
print(all_sites.nlargest(1,'IMDB_user_vote_count'))
print('-' * 75, '\n')


# O Filme com a maior quantidade de votos no Metacritic
print("Filme com mais votos no Metacritic\n")
print('-' * 75)
print(all_sites.nlargest(1,'Metacritic_user_vote_count'))
print('-' * 75, '\n')



# Mesclagem interna entre os df's fandango e all_sites baseando-se em 'FILM'

df_fan_sites = pd.merge(fandango,all_sites,on='FILM',how='inner')

print('Novo DataFrame: Dados mesclados (fandango + outros sites)')
print('Infos:')
print('-' * 75)
print(df_fan_sites.info())
print('-' * 75, '\n')

print('Exibição das 5 primeiras linhas do DataFrame')
print('-' * 75)
print(df_fan_sites.head())
print('-' * 75, '\n')



# Normalizando colunas para ESTRELAS e AVALIAÇÕES do fandango

# Normalizando RottenTomatoes
df_fan_sites['RT_Norm'] = np.round(df_fan_sites['RottenTomatoes']/20,1)
df_fan_sites['RTU_Norm'] = np.round(df_fan_sites['RottenTomatoes_User']/20,1)

# Normalizando Metacritic
df_fan_sites['Meta_Norm'] = np.round(df_fan_sites['Metacritic']/20,1)
df_fan_sites['Meta_U_Norm'] = np.round(df_fan_sites['Metacritic_User']/2,1)

# Normalizando IMDB
df_fan_sites['IMDB_Norm'] = np.round(df_fan_sites['IMDB']/2,1)

print('DataFrame com as notas normalizadas para o formato do fandango')
print('-' * 75)
print(df_fan_sites.head())
print('-' * 75, '\n')


# DataFrame das notas normalizadas
norm_scores = df_fan_sites[
    ['STARS','RATING','RT_Norm','RTU_Norm','Meta_Norm','Meta_U_Norm','IMDB_Norm']
]

print('Tabela das Notas Normalizadas')
print('-' * 75)
print(norm_scores.head())
print('-' * 75, '\n')


# Função para mover a legenda 
def move_legend(ax, new_loc, **kws):
    old_legend = ax.legend_
    handles = old_legend.legend_handles
    labels = [t.get_text() for t in old_legend.get_texts()]
    title = old_legend.get_title().get_text()
    ax.legend(handles, labels, loc=new_loc, title=title, **kws)


# Gráfico de comparação entre as notas normalizadas
print('Gerando gráfico: Comparação da distribuição das notas normalizadas\n')
print('-' * 75, '\n')

fig, ax = plt.subplots(figsize=(6.8,3.4), dpi=150)
sns.kdeplot(
    data=norm_scores, 
    clip=[0,5], 
    fill=True, 
    alpha=0.4, 
    palette='Set1', 
    ax=ax
)

move_legend(ax, 'upper left')
plt.savefig('plots/comparison_normalized_ratings.jpg')
plt.show()


# Gráfico de comparação entre as notas normalizadas de RT e do Fandango
print('Gerando gráfico: Comparação das notas do RT e do Fandango\n')
print('-' * 75, '\n')

fig, ax = plt.subplots(figsize=(6.8,3.4), dpi=150)
sns.kdeplot(
    data=norm_scores[['RT_Norm', 'STARS']], 
    clip=[0,5], 
    fill=True, 
    alpha=0.4, 
    palette='Set1', 
    ax=ax
)

move_legend(ax, 'upper left')
plt.savefig('plots/comparison_ratings_fandando_RT.jpg')
plt.show()


# Histograma de comparação entre as notas normalizadas de RT e do Fandango 
print(
    'Gerando gráfico (Histograma): Comparação das notas do normalizadas\n'
)
print('-' * 75, '\n')

plt.subplots(figsize=(6.8,3.4),dpi=150)
sns.histplot(norm_scores,bins=50)

plt.savefig('plots/comparison_ratings_histplot.jpg')
plt.show()

# Mapa de cluster com todas as notas normalizadas
print('Gerando gráfico (Cluster): Comparação das notas do normalizadas\n')
print('-' * 75, '\n')

g = sns.clustermap(norm_scores,cmap='magma',col_cluster=False)

plt.setp(g.ax_heatmap.get_xticklabels(), rotation=45)
g.savefig('plots/comparison_ratings_cluster.jpg')
plt.show()


# DataFrame com Notas Noremalizada e com o Nome dos Filmes
norm_films = df_fan_sites[[
    'STARS',
    'RATING',
    'RT_Norm',
    'RTU_Norm',
    'Meta_Norm',
    'Meta_U_Norm',
    'IMDB_Norm',
    'FILM'
]]


print('10 Filmes mais mal Avaliados')
print('-' * 75)
print(norm_films.nsmallest(10,'RT_Norm'))
print('-' * 75, '\n')


# Gráfico de Distribuição do top 10 piores avaliados
print('Gerando gráfico: Distribuição do top 10 piores avaliados\n')
print('-' * 75, '\n')

worst_films = norm_films.nsmallest(10,'RT_Norm').drop('FILM',axis=1)

plt.subplots(figsize=(6.8,3.4), dpi=150)
sns.kdeplot(
    data=worst_films, 
    clip=[0,5], 
    fill=True, 
    alpha=0.4, 
    palette='Set1'
)

plt.title("Rating for RT Ceitic's 10 Worst Reviewed Films")
plt.savefig('plots/ratings_top_10_worst_movies.jpg')
plt.show()