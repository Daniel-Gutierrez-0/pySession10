def borrow_movie(movie_list, title):
    for movie in movie_list:
        if movie[0] == (title)and(movie[3]):
            movie[3] = False
            return movie_list
    return movie_list
