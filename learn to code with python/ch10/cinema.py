# movies = []
# movie = {}

# movie['name'] = 'Forbidden Planet'
# movie['year'] = 1957
# movie['rating'] = '*****'
# movie['year'] = 1956

# movies.append(movie)

# movie2 = {
#     'name': 'I Was a Teenage Werewolf',
#     'year': 1957,
#     'rating': '****'
# }
# movie2['rating'] = '***'

# movies.append(movie2)

# movies.append({
#     'name': 'Viking Women and the Sea Serpant',
#     'year': 1957,
#     'rating': '**'
# })

# movies.append({
#     'name': 'Vertigo',
#     'year': 1958,
#     'rating': '*****'
# })

# print('Head First Movie Recommandations')
# print('--------------------------------')
# for movie in movies:
#     if len(movie['rating']) >= 4:
        # print(f"{movie['name']}({movie['rating']}) - {movie['year']}")


movies = {}
movie = {}

movie['name'] = 'Forbidden Planet'
movie['year'] = 1957
movie['rating'] = '*****'
movie['year'] = 1956

movies['Forbidden Planet'] = movie

movie2 = {
    'name': 'I Was a Teenage Werewolf',
    'year': 1957,
    'rating': '****'
}
movie2['rating'] = '***'
movies[movie2['name']] = movie2

movies['Viking Women and the Sea Serpent'] = {
    'name': 'Viking Women and the Sea Serpent',
    'year': 1957,
    'rating': '**'
}
movies['Vertigo'] = {
    'name': 'Vertigo',
    'year': 1958,
    'rating': '*****'
}
print('Head First Movie Recommandations')
print('--------------------------------')
for name in movies:
    movie = movies[name]
    if len(movie['rating']) >= 4:
        print(f"{movie['name']}({movie['rating']}) - {movie['year']}")

print()

print('Head First Movie Staff Pick')
print('---------------------------')
movie = movies['I Was a Teenage Werewolf']
print(f"{movie['name']}({movie['rating']}) - {movie['year']}")