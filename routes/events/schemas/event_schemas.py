from marshmallow import Schema, fields


class ContractSchema(Schema):
    contract_address = fields.Str(required=True)
    contract_abi = fields.List(fields.Dict, required=True)
    price_mark = fields.Float(required=True)
    asset_symbol = fields.Str(required=True)
    event_close = fields.Float(required=True)
    betting_close = fields.Float(required=True)

    class Meta:
        unknown = 'exclude'


class GetEventsSchema(Schema):
    data = fields.Nested(ContractSchema, required=True, many=True)
