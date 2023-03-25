from flask.views import MethodView
from flask_smorest import Blueprint, abort
from flask import current_app
from datetime import datetime, timedelta
from typing import Dict, Optional, List
from .schemas.event_schemas import GetEventsSchema

events_blueprint = Blueprint("events", __name__, url_prefix="/events", description="Events blueprint")


@events_blueprint.route("/current/6hr_events")
class CurrentEvents(MethodView):
    """
    Current 6hr events
    """

    @events_blueprint.response(status_code=200, schema=GetEventsSchema)
    def get(self) -> Optional[Dict]:
        db_client = current_app.extensions['mongodb_db']
        data = db_client.find(collection="event_contracts_6h",
                              query={"is_event_over": False,
                                     "event_close": {"$gt": datetime.now().timestamp()}})
        response_data = []
        for record in data:
            response_data.append(record)

        return {"data": response_data}
