from flask import current_app
from datetime import datetime


def find_active_events(event_type):
    data = []
    if event_type == "6hr_events":
        db_client = current_app.extensions['mongodb_db']
        data = db_client.find(collection="event_contracts_6h",
                              query={"is_event_over": False,
                                     "event_close": {"$gt": datetime.now().timestamp()}})
    if event_type == "12hr_events":
        db_client = current_app.extensions['mongodb_db']
        data = db_client.find(collection="event_contracts_12h",
                              query={"is_event_over": False,
                                     "event_close": {"$gt": datetime.now().timestamp()}})
    if event_type == "24hr_events":
        db_client = current_app.extensions['mongodb_db']
        data = db_client.find(collection="event_contracts_24h",
                              query={"is_event_over": False,
                                     "event_close": {"$gt": datetime.now().timestamp()}})
    if event_type == "test_events":
        db_client = current_app.extensions['mongodb_db']
        data = db_client.find(collection="event_contracts_test",
                              query={"is_event_over": False,
                                     "event_close": {"$gt": datetime.now().timestamp()}})

    response_data = []
    for record in data:
        response_data.append(record)

    return response_data


def find_payout_ready_events(wallet_address):
    payout_events = []
    db_client = current_app.extensions['mongodb_db']
    event_types = ["event_contracts_6h",
                   "event_contracts_12h",
                   "event_contracts_24h",
                   "event_contracts_test"]
    for event_type in event_types:
        records = db_client.find(collection=event_type,
                                 query={"is_event_over": True,
                                        "is_payout_period_over": False,
                                        "winning_betters_addresses": {"$in": [wallet_address]}
                                        })
        for record in records:
            payout_events.append(record)

    return payout_events
