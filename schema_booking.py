from schema import Schema, And, Use, Optional, SchemaError
import datetime


def schema(data):
    today = datetime.date.today()
    schema_json = Schema([{
        "firstname": And(str),
        "lastname": And(str),
        "totalprice": And(int, lambda n: 1 <= n <= 100000000000000),
        "depositpaid": And(bool),
        "bookingdates": {
            "checkin": And(str, lambda n: n >= today),
            "checkout": And(str, lambda n: n >= today)
        },
        "additionalneeds": And(str)
    }])
    if schema_json.validate(data):
        return True
    raise Exception("Невалидный JSON")
