from cw.dao.models import Genre, Director, Movie, User

from cw.config import DevelopmentConfig

from cw.server import create_app, db

app = create_app(DevelopmentConfig)


@app.shell_context_processor
def shell():
    return {
        "db": db,
        "Genre": Genre,
        "Director": Director,
        "Movie": Movie,
        "User": User,
    }
