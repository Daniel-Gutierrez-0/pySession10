# Group 6: Main Program Integration
def main_menu(movie_list):
    while True:
        print("1. Add movie")
        print("2. View available movies")
        print("3. Borrow movie")
        print("4. Return movie")
        print("5. Search movie")
        print("6. Exit")
        choice = input("Select an option: ")
        if choice == '1':
            title = input("Enter movie title: ")
            genre = input("Enter movie genre: ")
            year = int(input("Enter release year: "))
            available = input("Is the movie available (True/False): ")
            if available.lower() == 'true':
                available = True
            else:
                available = False
            add_movie(movie_list, title, genre, year, available)
            print(movie_list)

        elif choice == '2':
            print(movie_list)
            print(view_available_movies(movie_list))
        elif choice == '3':
            title = input("Enter movie title to borrow: ")
            borrow_movie(movie_list, title)
        elif choice == '4':
            title = input("Enter movie title to return: ")
            return_movie(movie_list, title)
        elif choice == '5':
            title = input("Enter movie title to search: ")
            print(search_movie(movie_list, title))
        elif choice == '6':
            break

# Sample movie list for testing
movie_list = [
    ["The Matrix", "Sci-Fi", 1999, True],
    ["The Godfather", "Crime", 1972, True],
    ["Titanic", "Romance", 1997, False]
]

# Start the program
main_menu(movie_list)
