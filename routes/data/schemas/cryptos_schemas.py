from marshmallow import Schema, fields


class DBPriceSchema(Schema):
    price = fields.Float(required=True)
    timestamp = fields.Float(required=True)

    class Meta:
        unknown = 'exclude'


class GetCryptoPricesSchema(Schema):
    data = fields.Nested(DBPriceSchema, required=True, many=True)


class GetCryptoLivePriceSchema(Schema):
    data = fields.Nested(DBPriceSchema, required=True)
