import pandas as df 
import numpy as np

games = df.read_csv('games_linked.csv')
platforms = df.read_csv('platforms_linked.csv')


#1.	Средние, медианные и максимальные продажи по каждому региону (NA, EU, JP, Global).
mean_games = games[['NA_Sales','EU_Sales','JP_Sales','Global_Sales']].mean()
print(f'Среднее продажи по каждому региону:\n{mean_games}')

median_games = games[['NA_Sales','EU_Sales','JP_Sales','Global_Sales']].median()
print(f'Медианные продажи по каждому региону:\n{median_games}')

max_games = games[['NA_Sales','EU_Sales','JP_Sales','Global_Sales']].max()
print(f'Максимальные продажи по каждому региону:\n{max_games}')

#2.	Топ-5 игр по общим продажам (Sales_Global).
top5 = (games.groupby('Name', as_index=False)['Global_Sales'].max().sort_values('Global_Sales', ascending=False).head(5))
print(f'Топ-5 игра по общим продажам:\n{top5}')

# 3. Получить список платформ с указанием производителя.(merge)
platform_list =df.merge(games,platforms,on=['Platform_ID','Platform_ID'],how='inner')   
platform_list_group = platform_list.groupby(['Platform','Manufacturer']).size().reset_index(name='Count')
print(f'Список платформ с указанием производителя:\n{platform_list_group}')

#4. Выяснить, какая платформа/производитель имеет самые большие средние продажи.
platform_list = df.merge(games,platforms,on=['Platform_ID','Platform_ID'],how='inner')   

platform_list_mean = (platform_list.groupby(['Platform','Manufacturer'], as_index= False)['Global_Sales'].mean()
                      .sort_values('Global_Sales', ascending=False).head(5))
print(f'Платформа/производитель с самымы бильшими средними продажами:\n{platform_list_mean}')

# 5. Посчитать суммарные продажи по платформам с учётом производителя.

platform_list = df.merge(games,platforms,on=['Platform_ID','Platform_ID'],how='inner')   

platform_list_mean = (platform_list.groupby(['Platform','Manufacturer'], as_index= False)['Global_Sales'].sum()
                      .sort_values('Global_Sales', ascending=False).head(5))
print(f'Суммарные продажи по платформам с учетом производителя:\n{platform_list_mean}')

# 6. Построить рейтинг жанров по средним и общим продажам

genre_rating = (games.groupby('Genre', as_index=False)['Global_Sales'].agg(mean_sales = 'mean', sum_sales = 'sum').reset_index()
                .sort_values('sum_sales',ascending=False).head(5))
print(f'Рейтинг жанров по средним и общим продажам:\n{genre_rating}')



