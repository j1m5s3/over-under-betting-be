from pymongo import MongoClient
from flask import current_app


class MongoDB:
    def __init__(self, app=None):
        self.client = None
        self.db = None

        self.app = app
        if app is not None:
            self.init_app(app)

    def init_app(self, app):
        uri = app.config['MONGO_DB_CONNECTION_STRING']
        self.client = MongoClient(uri)
        app.extensions['mongodb_client'] = self
        self.db = self.client[app.config['MONGO_DB_NAME']]
        app.extensions['mongodb_db'] = self

    def close(self):
        client = current_app.extensions['mongodb_client']
        client.close()

    def find_latest_price(self, collection):
        return self.db[collection].find_one(sort=[("timestamp", -1)])


