from cw.dao.genre import GenreDAO
from cw.dao.director import DirectorDAO
from cw.dao.movie import MovieDAO
from cw.dao.user import UserDAO
from cw.services.directors_service import DirectorsService
from cw.services.genres_service import GenresService
from cw.services.movies_service import MoviesService
from cw.services.users_service import UsersService
from cw.setup_db import db

movie_dao = MovieDAO(db.session)
director_dao = DirectorDAO(db.session)
genre_dao = GenreDAO(db.session)
user_dao = UserDAO(db.session)

movie_service = MoviesService(movie_dao)
director_service = DirectorsService(director_dao)
genre_service = GenresService(genre_dao)
user_service = UsersService(user_dao)
