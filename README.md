# Capstone Project – Análise Comparativa de Avaliações de Filmes  
Fandango • Rotten Tomatoes • Metacritic • IMDB

---

## Badges

![Status](https://img.shields.io/badge/status-completo-green)
![Python](https://img.shields.io/badge/Python-3.10+-blue)
![License](https://img.shields.io/badge/license-MIT-lightgrey)
![Data Science](https://img.shields.io/badge/category-data%20analysis-orange)

---

# Sumário

1. [Descrição Geral](#descrição-geral)  
2. [Estrutura do Projeto](#estrutura-do-projeto)  
3. [Tecnologias Utilizadas](#tecnologias-utilizadas)  
4. [Objetivos da Análise](#objetivos-da-análise)  
5. [Etapas da Análise](#etapas-da-análise)  
6. [Conclusões](#conclusões)  
7. [Como Executar](#como-executar)  
8. [Autor](#autor)

---

# Descrição Geral

Este projeto realiza uma análise detalhada das avaliações de filmes disponíveis em quatro plataformas: **Fandango**, **Rotten Tomatoes**, **Metacritic** e **IMDB**.

O foco principal está na avaliação da **confiabilidade das notas exibidas pelo Fandango**, comparando:

- **RATING** – a nota real utilizada internamente pela plataforma  
- **STARS** – a nota exibida ao público em forma de estrelas  

Além disso, o projeto compara as avaliações externas para identificar padrões, consistência entre críticos e usuários, além de possíveis vieses entre as plataformas.

---

# Estrutura do Projeto

```
.
├── data/
│   ├── fandango_scrape.csv
│   └── all_sites_scores.csv
│
├── scripts/
│   └── projeto.py
│
├── plots/
│   ├── rating_vs_votes.jpg
│   ├── contagem_por_ano.jpg
│   ├── rating_vs_stars.jpg
│   ├── stars_diff_cout.jpg
│   ├── RT_critic_vs_users.jpg
│   ├── RT_critics_minus_RT_users.jpg
│   ├── abs_RT_critics_minus_RT_users.jpg
│   ├── MC_critic_vs_users.jpg
│   ├── user_vote_count_Metacritic_vs_IMDB.jpg
│   ├── comparison_normalized_ratings.jpg
│   ├── comparison_ratings_fandando_RT.jpg
│   ├── comparison_ratings_histplot.jpg
│   ├── comparison_ratings_cluster.jpg
│   ├── ratings_top_10_worst_movies.jpg
│   └── ...
│
├── requirements.txt
└── README.md
```

---

# Tecnologias Utilizadas

- Python 3.x  
- Pandas  
- NumPy  
- Seaborn  
- Matplotlib  

---

# Objetivos da Análise

- Avaliar possíveis inconsistências entre as notas internas e exibidas pelo Fandango.  
- Comparar avaliações de usuários e críticos em várias plataformas.  
- Normalizar métricas distintas para permitir comparações diretas.  
- Identificar discrepâncias extremas entre as plataformas.  
- Gerar visualizações para apoiar conclusões estatísticas.  

---

# Etapas da Análise

## 1. Exploração Inicial dos Dados  
Inclui:

- Inspeção de colunas  
- Estatísticas descritivas  
- Correlações  
- Extração do ano dos filmes  
- Contagem de filmes por ano  

---

## 2. Avaliação do Fandango  
Esta é a parte central do projeto.

Pontos analisados:

- Relação entre **RATING** e número de votos  
- Diferença entre **STARS** (nota exibida) e **RATING** (nota real)  
- Cálculo da coluna:  
  ```
  STARS_DIFF = STARS - RATING
  ```
- Distribuição das diferenças entre as notas  
- Identificação de filmes com discrepâncias de 1 ponto ou mais  
- Avaliação de padrão sistemático de inflação de notas  

---

## 3. Análises das Plataformas Externas

### Rotten Tomatoes  
- Diferença entre críticos e usuários  
- Diferença absoluta média  
- Filmes com maior divergência  

### Metacritic  
- Comparação entre crítica e usuários  
- Tendência geral e consistência  

### IMDB  
- Relação entre quantidade de votos e nota média  
- Filme com maior volume de avaliações  

---

## 4. Mesclagem dos Dados Consolidados  

A junção entre Fandango e All Sites é feita por:

```python
df_fan_sites = pd.merge(fandango, all_sites, on='FILM', how='inner')
```

Isso permite estudar cada filme sob várias plataformas simultaneamente.

---

## 5. Normalização das Escalas  

Todas as plataformas foram convertidas para a escala **0–5**, ajustando:

- Rotten Tomatoes (críticos e usuários): /20  
- Metacritic (críticos): /20  
- Metacritic User: /2  
- IMDB: /2  

As notas do Fandango já estão nessa faixa.

---

## 6. Comparações Entre Plataformas  

Após a normalização:

- Comparações diretas entre todas as métricas  
- Análises de agrupamento (cluster)  
- Verificação de proximidade entre plataformas  
- Comparação direta entre Fandango e Rotten Tomatoes  
- Análise dos 10 piores filmes segundo críticos  

---

# Conclusões

As conclusões desta análise foram elaboradas com foco especial no **comportamento das notas do Fandango**, conforme solicitado.

---

## 1. O Fandango apresenta indícios fortes de inflação de notas

A comparação entre **RATING** (nota interna real) e **STARS** (nota exibida ao usuário) mostra:

- A grande maioria dos filmes possui **STARS > RATING**  
- Diferenças frequentes entre **0.3 e 0.6 pontos**  
- Vários casos extremos com **1 ponto de discrepância**

Essa diferença é sistemática e sempre favorece uma nota maior ao público, indicando que o Fandango ajusta ou arredonda positivamente as notas.

Não há justificativa técnica para que STARS e RATING sejam diferentes, já que ambas deveriam representar a mesma avaliação.

---

## 2. Ao comparar com outras plataformas, o Fandango se destaca por ser mais benevolente

Depois da normalização:

- O Fandango é consistentemente a plataforma com maiores notas.  
- Ele se alinha mais a IMDB, que tende a ter avaliações mais generosas, e se distancia dos sites de crítica tradicional.  
- Rotten Tomatoes Critics e Metacritic apresentam avaliações mais rígidas.

Isso reforça que o Fandango “puxa para cima” a percepção de qualidade dos filmes.

---

## 3. O padrão de inflação ocorre independentemente da qualidade do filme

Mesmo nos filmes amplamente mal avaliados:

- O Fandango mantém notas relativamente altas  
- A tendência de inflação é mantida  
- Outras plataformas convergem para avaliações baixas, mas o Fandango se destaca por ser mais positivo

Isso demonstra que o viés não depende do tipo ou categoria do filme, mas sim faz parte da metodologia geral da plataforma.

---

## 4. STARS e RATING não são equivalentes, apesar de representarem a mesma métrica

Nas outras plataformas:

- A nota exibida ao público é a mesma nota real  
- Não há dupla representação com valores diferentes  

No Fandango:

- Há duas métricas distintas para a mesma avaliação  
- A exibida ao público é sistematicamente modificada positivamente

Essa duplicidade reforça a hipótese de um **viés de apresentação**.

---

## 5. A análise evidencia diferenças estruturais entre as plataformas

Enquanto:

- **Fandango** → exibe notas consistentemente mais altas  
- **IMDB** → notas mais altas, porém com forte variação baseada em número de votos  
- **Rotten Tomatoes** e **Metacritic** → avaliações rígidas e coerentes entre crítica e notas normalizadas

Fica claro que o Fandango segue um padrão próprio de avaliação, significativamente mais generoso.

---

# Como Executar

## 1. Instale as dependências

Na raiz do projeto:

```bash
pip install -r requirements.txt
```

---

## 2. Execute o script principal

```bash
python scripts/projeto.py
```

Os gráficos serão gerados automaticamente na pasta:

```
plots/
```

---

# Autor

**Alessandro Moreira Cecilio**
