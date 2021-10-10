import pandas as pd

'''
download data from here
https://github.com/wesm/pydata-book/tree/2nd-edition/datasets/movielens
'''
mnames = ['movie_id', 'title', 'genres']

movies = pd.read_table('movies.dat',  sep='::',
                       header=None, names=mnames)
unames = ['user_id', 'gender', 'age', 'occupation', 'zip']
users = pd.read_table('users.dat', sep='::',
                      header=None, names=unames)

rnames = ['user_id', 'movie_id', 'rating', 'timestamp']
ratings = pd.read_table('ratings.dat', sep='::',
                        header=None, names=rnames)

data = pd.merge(pd.merge(ratings, users), movies)

mean_ratings = data.groupby(['title', 'gender']).mean()['rating']
#mean_ratings = data.groupby(['title', 'gender']).agg(['mean'])['rating']

print(mean_ratings)
print('#' * 70)
print(mean_ratings.unstack())
# all of above can also be done by pivot table method
mean_ratings_pivot_table = data.pivot_table('rating', index='title', columns='gender', aggfunc='mean')
print(mean_ratings_pivot_table)
print('#' * 70)
# find all the movie titles having rating more than 250
ratings_by_title = data.groupby(['title']).size().reset_index().rename(columns={0: 'count_of_ratings'})
active_ratings = ratings_by_title[ratings_by_title['count_of_ratings'] > 250].set_index('title')
print(active_ratings)
print('#' * 70)

# now select those titles by active_ratings
print(mean_ratings_pivot_table.loc[active_ratings.index])
print('#' * 70)
# top ratings for females
print(mean_ratings.sort_values(by='F', ascending=False))