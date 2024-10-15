#code for viewing movies available
def view_available_movies(movie_list):
    return [movie for movie in movie_list if movie[3] == True]