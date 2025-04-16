import logging
from flask import Flask, jsonify
from flask_cors import CORS, cross_origin
from flasgger import Swagger
from controllers import tournaments, players, events, h2h, ranking

app = Flask(__name__)
app.config["CORS_HEADERS"] = "Content-Type"

template = {
    "swagger": "2.0",
    "info": {
        "title": "BrainBets API",
        "description": "This API was developed using Python Flask, which provides an interface for producing and consuming BrainBets Tennis data",
        "version": "1.0",
    },
}
app.config["SWAGGER"] = {
    "title": "BrainBets API",
    "uiversion": 2,
    "template": "./resources/flasgger/swagger_ui.html",
}
Swagger(app, template=template)

app.register_blueprint(tournaments.tournaments_api)
app.register_blueprint(players.players_api)
app.register_blueprint(events.events_api)
app.register_blueprint(h2h.h2h_api)
app.register_blueprint(ranking.ranking_api)

cors = CORS(app)

logging.basicConfig(filename="test.log", level=logging.DEBUG)

VERSION = "1.0"


@app.route("/", methods=["GET"])
@cross_origin()
def spec():
    return "BRAINBEST API"


if __name__ == "__main__":
    app.run()
