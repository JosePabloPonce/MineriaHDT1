import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import plotly.express as px

# para probar los ejercicios es necesario descomentarlos 
# para ver el resultado ya sea del ejercicio o del grafico

movies = pd.read_csv("movies.csv")

#4.1 ¿Cuáles son las 10 películas que contaron con más presupuesto?
a = movies.nlargest(10, 'budget')['title']
# print(a)

#4.2 ¿Cuáles son las 10 películas que contaron con más ganancias?
b = movies.nlargest(10, 'revenue')['title']
# print(b)

#4.3 ¿Cuál es la película que más votos tuvo?
c = movies.nlargest(10, 'voteCount')['title']
# print(c)

#4.4 ¿Cuál es la peor película de acuerdo a los votos de todos los usuarios?
d = movies.nlargest(10, 'voteAvg')['title']
# print(d)

#4.5 ¿Cuántas películas se hicieron en cada año? 
# ¿En qué año se hicieron más películas? 
# Haga un gráfico de barras
movies['releaseDate'] = pd.to_datetime(movies['releaseDate'])
releaseDt = movies['releaseDate'].dt.year.value_counts()
#graph
# ejeX = np.array(pd.value_counts(pd.to_datetime(movies.releaseDate).dt.year).keys())
# ejeY = pd.value_counts(pd.to_datetime(movies.releaseDate).dt.year)
# plt.bar(ejeX, ejeY)
# plt.title("Movies by year")
# plt.rcParams['figure.figsize'] = (10, 10)
# print(releaseDt)
# plt.show()

#4.6 ¿Cuál es el género principal de las 20 películas más recientes? 
# ¿Cuál es el género principal que predomina en el conjunto de datos? 
# Represéntelo usando un gráfico
movies['genre1'] = movies['genres'].str.split('|', n=-1).str[0]
top_movies = movies.sort_values('releaseDate', ascending=False)[['title', 'genre1', 'releaseDate']].head(20)
# print(top_movies)
top20genres = pd.value_counts(top_movies.genre1)
# print(top20genres)
#graph
# ejeX = np.array(top20genres.keys())
# ejeY = top20genres
# plt.rcParams['figure.figsize'] = (20, 20)
# plt.bar(ejeX, ejeY)
# plt.title("Top 20 movies by genre")
# plt.show()

# 4.7 ¿Las películas de qué genero principal obtuvieron mayores ganancias?
topRevenue = movies.sort_values('revenue', ascending=False)[['title', 'genre1', 'revenue']].head(30)
# print(topRevenue)




#4.12
#se agrega una nueva columna que solo posee el mes de lanzamiento
movies['Month'] = pd.to_datetime(movies['releaseDate']).dt.strftime('%m')
#se realiza un diagrama de barras
fig = px.bar(movies, x = 'Month', y = 'revenue', title='Fecha de estreno vs Ingresos',)
fig.show()
#se realiza un diagrama de cajas y bigotes
fig2 = px.box(movies, x = 'Month', y = 'revenue', title='Fecha de estreno vs Ingresos',)
fig2.show()


# 4.13
# se cambia el formato
movies['releaseDate'] = pd.to_datetime(movies.releaseDate, format='%Y-%m-%d')
# se agrega columna yyyy-mm
movies['month_year'] = movies['releaseDate'].dt.to_period('M')
# se cuenta las peliculas por yyyy-mm y se crea nuevo dataframe
df2 = movies['month_year'].value_counts().rename_axis('month_year').reset_index(name='counts')
df2['month'] = df2['month_year'].dt.month
#se obtiene la mean, min y max de peliculas estrenadas en cada mes
grouped_single = df2.groupby('month').agg({'counts': ['mean', 'min', 'max']})
#print(grouped_single)

#4.14
#se realiza un diagrama de dispersion para ver la correlacion
fig = px.scatter(movies, x = 'voteCount', y = 'revenue', title='voteCount vs revenue')
fig.show()
#print(np.corrcoef(movies['voteCount'], movies['revenue'])[0])


#4.15
#se realiza un split para solo dejar el genero principal
movies['genres'] = movies['genres'].str.split('|', expand = True,n=1)
#se obtienen las 100 peliculas mas largas y se hace un conteo por cada genero
df2= (movies.nlargest(100, 'runtime')['genres'].value_counts())
#print(df2)
