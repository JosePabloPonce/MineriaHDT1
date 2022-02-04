import pandas as pd
import plotly.express as px

movies = pd.read_csv("movies.csv")

#ejercicio12
#se agrega una nueva columna que solo posee el mes de lanzamiento
movies['Month'] = pd.to_datetime(movies['releaseDate']).dt.strftime('%m')

#se realiza un diagrama de barras
fig = px.bar(movies, x = 'Month', y = 'revenue', title='Fecha de estreno vs Ingresos',)
fig.show()

#se realiza un diagrama de cajas y bigotes
fig2 = px.box(movies, x = 'Month', y = 'revenue', title='Fecha de estreno vs Ingresos',)
fig2.show()


#ejercicio13
#se cambia el formato
movies['releaseDate'] = pd.to_datetime(movies.releaseDate, format='%Y-%m-%d')

#se agrega columna yyyy-mm
movies['month_year'] = movies['releaseDate'].dt.to_period('M')

#se cuenta las peliculas por yyyy-mm y se crea nuevo dataframe
df2 = movies['month_year'].value_counts().rename_axis('month_year').reset_index(name='counts')
df2['month'] = df2['month_year'].dt.month

#se obtiene la mean, min y max de peliculas estrenadas en cada mes
grouped_single = df2.groupby('month').agg({'counts': ['mean', 'min', 'max']})
print(grouped_single)

#ejercicio14
#se realiza un diagrama de dispersion para ver la correlacion
fig = px.scatter(movies, x = 'voteCount', y = 'revenue', title='voteCount vs revenue')
fig.show()

#ejercicio15
#se realiza un split para solo dejar el genero principal
movies['genres'] = movies['genres'].str.split('|', expand = True,n=1)

#se obtienen las 100 peliculas mas largas y se hace un conteo por cada genero
df2= (movies.nlargest(100, 'runtime')['genres'].value_counts())
print(df2)
