from sqlalchemy.exc import IntegrityError


from config import DevelopmentConfig
from dao.models import Director, Genre, Movie

from server import create_app
from setup_db import db
from utils import read_json

app = create_app(DevelopmentConfig)

data = read_json( "fixtures.json" )

with app.app_context():
    for genre in data["genres"]:
        db.session.add(Genre(id=genre["pk"], name=genre["name"]))

    for director in data["directors"]:
        db.session.add(Director(id=director["pk"], name=director["name"]))

    for movie in data["movies"]:
        db.session.add(Movie(id=movie["pk"],
                             title=movie["title"],
                             description=movie["description"],
                             trailer=movie["trailer"],
                             year=movie["year"],
                             rating=movie["rating"],
                             genre_id=movie["genre_id"],
                             director_id=movie["director_id"]))

    try:
        db.session.commit()
    except IntegrityError:
        print("Fixtures already loaded")
