from flask.views import MethodView
from flask_smorest import Blueprint
from typing import Dict, Optional
from .schemas.event_schemas import GetEventsSchema
from .utils.mongo_utils import find_active_events, find_payout_ready_events

events_blueprint = Blueprint("events", __name__, url_prefix="/events", description="Events blueprint")


@events_blueprint.route("/withdraw/<wallet_address>")
class PayoutReadyEvents(MethodView):
    """
    Withdrawable events for the given wallet address
    :param event_type: 6hr_events, 12hr_events, 24hr_events, test_events
    :param wallet_address: 0x1234, etc
    """
    # TODO: Add new schema to handle records from all potential event types
    @events_blueprint.response(status_code=200, schema=GetEventsSchema)
    def get(self, wallet_address: str) -> Optional[Dict]:
        data = find_payout_ready_events(wallet_address)
        return {"data": data}


@events_blueprint.route("/current/6hr_events")
class Current6hrEvents(MethodView):
    """
    Active 6hr events
    """
    @events_blueprint.response(status_code=200, schema=GetEventsSchema)
    def get(self) -> Optional[Dict]:
        event_type = "6hr_events"
        data = find_active_events(event_type)
        return {"data": data}


@events_blueprint.route("/current/12hr_events")
class Current12hrEvents(MethodView):
    """
    Active 12hr events
    """
    @events_blueprint.response(status_code=200, schema=GetEventsSchema)
    def get(self) -> Optional[Dict]:
        event_type = "12hr_events"
        data = find_active_events(event_type)
        return {"data": data}


@events_blueprint.route("/current/24hr_events")
class Current24hrEvents(MethodView):
    """
    Active 24hr events
    """
    @events_blueprint.response(status_code=200, schema=GetEventsSchema)
    def get(self) -> Optional[Dict]:
        event_type = "24hr_events"
        data = find_active_events(event_type)
        return {"data": data}


@events_blueprint.route("/current/test_events")
class CurrentTestEvents(MethodView):
    """
    Active test events
    """
    @events_blueprint.response(status_code=200, schema=GetEventsSchema)
    def get(self) -> Optional[Dict]:
        event_type = "test_events"
        data = find_active_events(event_type)
        return {"data": data}



