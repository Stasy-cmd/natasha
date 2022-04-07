from dao.genre import GenreDAO
from dao.director import DirectorDAO
from dao.movie import MovieDAO
from dao.user import UserDAO
from services.directors_service import DirectorsService
from services.genres_service import GenresService
from services.movies_service import MoviesService
from services.users_service import UsersService
from setup_db import db

movie_dao = MovieDAO(db.session)
director_dao = DirectorDAO(db.session)
genre_dao = GenreDAO(db.session)
user_dao = UserDAO(db.session)

movie_service = MoviesService(movie_dao)
director_service = DirectorsService(director_dao)
genre_service = GenresService(genre_dao)
user_service = UsersService(user_dao)
