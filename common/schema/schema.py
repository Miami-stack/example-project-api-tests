from schema import Schema


class ClassSchema:
    def validate_json_post(data):
        schema_json = Schema({"bookingid": int, "booking": {
            "firstname": str,
            "lastname": str,
            "totalprice": int,
            "depositpaid": bool,
            "bookingdates": {
                "checkin": str,
                "checkout": str,
            },
            "additionalneeds": str
        }})

        if schema_json.validate(data):
            return True
        raise Exception("Невалидный JSON")

    def validate_json_get(data):
        schema_json = Schema({
            "firstname": str,
            "lastname": str,
            "totalprice": int,
            "depositpaid": bool,
            "bookingdates": {
                "checkin": str,
                "checkout": str,
            },
            "additionalneeds": str
        })

        if schema_json.validate(data):
            return True
        raise Exception("Невалидный JSON")
