import logging
from flask import Flask
from flask_cors import CORS, cross_origin
from flasgger import Swagger
from controllers import team_stadistics

app = Flask(__name__)
app.config["CORS_HEADERS"] = "Content-Type"

template = {
    "swagger": "2.0",
    "info": {
        "title": "BrainBets API",
        "description": "This API provides an interface for producing and consuming BrainBets Football data",
        "version": "1.0",
    },
}
app.config["SWAGGER"] = {
    "title": "BrainBets API",
    "uiversion": 2,
    "template": "./resources/flasgger/swagger_ui.html",
}
Swagger(app, template=template)

app.register_blueprint(team_stadistics.team_stadistics_api)

cors = CORS(app)

logging.basicConfig(filename="test.log", level=logging.DEBUG)

VERSION = "1.0"

@app.route("/", methods=["GET"])
@cross_origin()
def spec():
    return "BRAINBEST API"

if __name__ == "__main__":
    app.run()
