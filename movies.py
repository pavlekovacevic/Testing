movies = [
{
"name": "Usual Suspects", 
"imdb": 7.0,
"category": "Thriller"
},
{
"name": "Hitman",
"imdb": 6.3,
"category": "Action"
},
{
"name": "Dark Knight",
"imdb": 9.0,
"category": "Adventure"
},
{
"name": "The Help",
"imdb": 8.0,
"category": "Drama"
},
{
"name": "The Choice",
"imdb": 6.2,
"category": "Romance"
},
{
"name": "Colonia",
"imdb": 7.4,
"category": "Romance"
},
{
"name": "Love",
"imdb": 6.0,
"category": "Romance"
},
{
"name": "Bride Wars",
"imdb": 5.4,
"category": "Romance"
},
{
"name": "AlphaJet",
"imdb": 3.2,
"category": "War"
},
{
"name": "Ringing Crime",
"imdb": 4.0,
"category": "Crime"
},
{
"name": "Joking muck",
"imdb": 7.2,
"category": "Comedy"
},
{
"name": "What is the name",
"imdb": 9.2,
"category": "Suspense"
},
{
"name": "Detective",
"imdb": 7.0,
"category": "Suspense"
},
{
"name": "Exam",
"imdb": 4.2,
"category": "Thriller"
},
{
"name": "We Two",
"imdb": 7.2,
"category": "Romance"
}
]

def is_movie_higher_5(movie):
    if(movie['imdb'] > 5.5):
        return True
    else:
        return False
"""Second task"""

def sublist_of_movies_higher_5(movies):
    sublist = []
    for movie in movies:
        movie_score = movie.get('imdb')
        movie_title = movie.get('name')
        if movie_score > 5.5:
            sublist.append(movie_title)


"""third task"""
def sorted_by_category(movies,category):
    for movie in movies:
        movie_category = movie.get('category')
        movie_titles = movie.get('name')
        if movie_category == category:
            return movie_titles

"""fourth task"""

def avg_imdb_for_all(movies):
    avg_score = 0
    for movie in movies:
        movie_score = movie.get('imdb')
        avg_score = avg_score + movie_score
        avg_score1 = avg_score / len(movies) 
    return avg_score1
    

"""fifth task"""

def score_in_single_category(movies, category):
    avg_score = 0
    list = []
    for movie in movies:
        movie_category = movie.get('category')
        movie_score = movie.get('imdb')
        movie_title = movie.get('name')
        if movie_category == category:
            list.append(movie_title)
            avg_score = avg_score + movie_score
            avg1 = avg_score / len(list)
    return avg1
        


