def favorite_movie(name):
    """Function make answer with argument 'name'.
    """
    answer = f'My favorite movie is named {name}.'
    print(answer)


if __name__ == '__main__':
    movie_name = input('Enter, please, the name of your favourite movie: ')
    favorite_movie(movie_name)
