from flask_restx import abort, Namespace, Resource

from cw.exceptions import ItemNotFound
from cw.services import DirectorsService
from cw.setup_db import db

directors_ns = Namespace("directors")


@directors_ns.route("/")
class DirectorsView(Resource):
    @directors_ns.response(200, "OK")
    def get(self):
        return DirectorsService(db.session).get_all_directors()


@directors_ns.route("/<int:director_id>")
class GenreView(Resource):
    @directors_ns.response(200, "OK")
    @directors_ns.response(404, "Director is not found")
    def get(self, genre_id: int):
        try:
            return DirectorsService(db.session).get_one_by_id(genre_id)
        except ItemNotFound:
            abort(404, message="Director is not found")
