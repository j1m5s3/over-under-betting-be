from flask import Flask, request
from flask_smorest import Api

from dotenv import find_dotenv, dotenv_values

from db.mongodb import MongoDB
from routes.data.cryptos import cryptos_blueprint

config = dotenv_values(dotenv_path=find_dotenv())

app = Flask(__name__)

# TODO: Move configurations to Config class
app.config["API_TITLE"] = "My API"
app.config["API_VERSION"] = "v1"
app.config["OPENAPI_VERSION"] = "3.0.2"
app.config["OPENAPI_URL_PREFIX"] = "/"
app.config["OPENAPI_SWAGGER_UI_PATH"] = "/swagger-ui"
app.config["OPENAPI_SWAGGER_UI_URL"] = "https://cdn.jsdelivr.net/npm/swagger-ui-dist/"

app.config["MONGO_DB_CONNECTION_STRING"] = config["MONGO_DB_CONNECTION_STRING"]
app.config["MONGO_DB_NAME"] = config["MONGO_DB_NAME"]

api = Api(app)
db = MongoDB(app)

api.register_blueprint(cryptos_blueprint)


# log request and response
@app.after_request
def log_request_and_response(response):
    # log request
    if request.method == "GET":
        app.logger.info(f"Request: {request.method} {request.url} {request.args}")
    if request.method == "POST":
        app.logger.info(f"Request: {request.method} {request.url}, {request.json}")

    # log response
    app.logger.info(f"Response: {response.status} {response.json}")

    return response


if __name__ == '__main__':
    app.run(host="localhost", port=8000, debug=True)
    pass
