from flask import Flask, request
from flask_smorest import Api

from dotenv import find_dotenv, dotenv_values

from db.mongodb import MongoDB
from routes.data.cryptos import cryptos_blueprint

config = dotenv_values(dotenv_path=find_dotenv())

app = Flask(__name__)

# TODO: Move configurations to Config class
app.config["API_TITLE"] = "Over Under Betting API"
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
    request_bound = f"##########################-REQUEST-###########################"
    response_bound = f"##########################-RESPONSE-##########################"
    end_bound = f"##########################-END-###############################"
    # log request
    if request.method == "GET":
        app.logger.info(request_bound)
        app.logger.info(f"method: {request.method}")
        app.logger.info(f"url: {request.url}")
        app.logger.info(f"args: {request.args.__dict__}")
    if request.method == "POST":
        app.logger.info(request_bound)
        app.logger.info(f"method: {request.method}")
        app.logger.info(f"url: {request.url}")
        app.logger.info(f"json: {request.json}")

    # log response
    app.logger.info(response_bound)
    app.logger.info(f"status: {response.status}")
    app.logger.info(f"json: {response.json}")
    app.logger.info(end_bound)

    return response


@app.route("/")
def health_check():
    return {"status": "OK", "message": "Over Under Betting API is up and running"}


if __name__ == '__main__':
    app.run(host="localhost", port=8000, debug=True)
    pass
