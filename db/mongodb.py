from pymongo import MongoClient
from flask import current_app

from datetime import datetime, timedelta


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

    def find_hourly_series(self, collection, num_hours):
        now = datetime.now()
        dt_before_now = now - timedelta(hours=num_hours)

        end_timestamp = now.timestamp()
        start_timestamp = dt_before_now.timestamp()

        query = {"timestamp": {"$gte": start_timestamp,
                               "$lt": end_timestamp,
                               "$mod": [60, 0]}}

        return self.db[collection].find(query)


