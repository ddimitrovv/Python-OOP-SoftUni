import os

from project.user import User


class MovieApp:
    def __init__(self):
        self.movies_collection = []
        self.users_collection = []

    def __check_if_user_exists(self, username):
        for user in self.users_collection:
            if user.username == username:
                return True
        return False

    def __check_if_movie_exists(self, title):
        for movie in self.movies_collection:
            if movie.title == title:
                return True
        return False

    def __check_if_user_liked_movie(self, username, movie_title):
        for user in self.users_collection:
            if user.username == username:
                for movie in user.movies_liked:
                    if movie.title == movie_title:
                        return True
        return False

    def register_user(self, username, age):
        if self.__check_if_user_exists(username):
            raise Exception('User already exists!')
        new_user = User(username, age)
        self.users_collection.append(new_user)
        return f'{username} registered successfully.'

    def upload_movie(self, username, movie):
        if not self.__check_if_user_exists(username):
            raise Exception('This user does not exist!')
        elif self.__check_if_movie_exists(movie.title):
            raise Exception('Movie already added to the collection!')
        elif not username == movie.owner.username:
            raise Exception(f'{username} is not the owner of the movie {movie.title}!')
        else:
            self.movies_collection.append(movie)
            for user in self.users_collection:
                if user.username == username:
                    user.movies_owned.append(movie)
                    return f'{username} successfully added {movie.title} movie.'

    def edit_movie(self, username, movie, **kwargs):
        if not self.__check_if_movie_exists(movie.title):
            raise Exception(f'The movie {movie.title} is not uploaded!')
        elif not username == movie.owner.username:
            raise Exception(f'{username} is not the owner of the movie {movie.title}!')
        else:
            for attr, new_value in kwargs.items():
                setattr(movie, attr, new_value)
            return f'{username} successfully edited {movie.title} movie.'

    def delete_movie(self, username, movie):
        if not self.__check_if_movie_exists(movie.title):
            raise Exception(f'The movie {movie.title} is not uploaded!')
        elif not username == movie.owner.username:
            raise Exception(f'{username} is not the owner of the movie {movie.title}!')
        else:
            self.movies_collection.pop(self.movies_collection.index(movie))
            for user in self.users_collection:
                if user.username == username:
                    user.movies_owned.pop(user.movies_owned.index(movie))
                    return f'{username} successfully deleted {movie.title} movie.'

    def like_movie(self, username, movie):
        if username == movie.owner.username:
            raise Exception(f'{username} is the owner of the movie {movie.title}!')
        elif self.__check_if_user_liked_movie(username, movie.title):
            raise Exception(f'{username} already liked the movie {movie.title}!')
        else:
            movie.likes += 1
            for user in self.users_collection:
                if user.username == username:
                    user.movies_liked.append(movie)
            return f'{username} liked {movie.title} movie.'

    def dislike_movie(self, username, movie):
        if not self.__check_if_user_liked_movie(username, movie.title):
            raise Exception(f'{username} has not liked the movie {movie.title}!')
        else:
            movie.likes -= 1
            for user in self.users_collection:
                if user.username == username:
                    user.movies_liked.pop(user.movies_liked.index(movie))
            return f'{username} disliked {movie.title} movie.'

    def display_movies(self):
        if len(self.movies_collection) == 0:
            return 'No movies found.'
        else:
            result_str = []
            for movie in sorted(self.movies_collection, key=lambda x: (-x.year, x.title)):
                result_str.append(movie.details())
            return os.linesep.join(result_str)

    def __str__(self):
        users = ', '.join([user.username for user in self.users_collection]) if\
            self.users_collection else 'No users.'
        movies = ', '.join([movie.title for movie in self.movies_collection]) if\
            self.movies_collection else 'No movies.'

        return f'All users: {users}' + os.linesep + f'All movies: {movies}'
