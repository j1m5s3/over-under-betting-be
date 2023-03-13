from flask.views import MethodView
from flask_smorest import Blueprint, abort
from flask import current_app

from typing import Dict, Optional, List
from .schemas.cryptos_schemas import GetCryptoPricesSchema, GetCryptoLivePriceSchema


cryptos_blueprint = Blueprint("cryptos", __name__, url_prefix="/data", description="Cryptos blueprint")


@cryptos_blueprint.route("<crypto_symbol>/price/latest")
class CryptosPrice(MethodView):
    """
    Cryptos price
    :param crypto_symbol: BTC, ETH, etc
    """

    @cryptos_blueprint.response(status_code=200, schema=GetCryptoLivePriceSchema)
    def get(self, crypto_symbol: str) -> Optional[Dict]:
        symbol = crypto_symbol.upper()
        db_client = current_app.extensions['mongodb_db']
        if symbol not in ["BTC", "ETH"]:
            abort(400, message="Invalid crypto symbol")
        else:
            if symbol == "BTC":
                data = db_client.find_latest_price("btc_live_price")
            if symbol == "ETH":
                data = db_client.find_latest_price("eth_live_price")

        return {"data": data}
