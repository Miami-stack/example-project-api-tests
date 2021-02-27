from model.booking import BookingData
from common.schema.schema import ClassSchema
import pytest


class TestCreateBooking:
    def test_create_booking(self, client):
        """
        Отправка запроса 'create_booking' с валидными данными
        """
        data = BookingData().random()
        res = client.create_booking(data)
        assert res.status_code == 200
        assert ClassSchema.validate_json_post(res.json())
        booking_info = res.json()
        assert booking_info.get('booking') == data

    @pytest.mark.skip(reason="Ошибка в апи")
    @pytest.mark.parametrize("field, value", [
        ['firstname', 21], ['lastname', 34],
        ['additionalneeds', 45]
    ])
    def test_invalid_string_create_booking(self, field, value, client):
        """
        Отправка запроса 'create_booking' с невалидными полями
         'firstname' , 'lastname', 'additionalneeds'
        """
        data = BookingData().random()
        setattr(data, field, value)
        res = client.create_booking(data)
        assert res.status_code == 200
        booking_info = res.json()
        assert booking_info.get('booking') == data

    def test_invalid_date_create_booking(self, client):
        """
        Отправка запроса 'create_booking' с датой заезда будущего времени
        и с датой выезда прошлого времени ("2040-01-01" и "2002-01-01")
        """
        data = BookingData().random()
        data.bookingdates.checkin = "2040-01-01"
        data.bookingdates.checkout = "2002-01-01"
        # TODO сгенерировать с помощью библиотеки питон
        res = client.create_booking(data)
        assert res.status_code == 200
        booking_info = res.json()
        assert booking_info.get('booking') == data

    @pytest.mark.parametrize("value", [0, -1])
    def test_invalid_total_price_create_booking(self, client, value):
        data = BookingData().random()
        setattr(data, 'totalprice', value)
        res = client.create_booking(data)
        assert res.status_code == 200
        booking_info = res.json()
        assert booking_info.get('booking') == data

    @pytest.mark.skip(reason="Значение 0.15 ломает тест")
    @pytest.mark.parametrize("value", [0.15, 1, 1000, 1000000])
    def test_invalid_float_value_total_price_create_booking(self, client, value):
        data = BookingData().random()
        setattr(data, 'totalprice', value)
        res = client.create_booking(data)
        assert res.status_code == 200
        booking_info = res.json()
        assert booking_info.get('booking') == data

    @pytest.mark.skip(reason="Тест ломается на значение totalprice")
    def test_invalid_more_value_total_price_create_booking(self, client):
        data = BookingData().random()
        setattr(data, 'totalprice', '10000000000000000000000000')
        res = client.create_booking(data)
        assert res.status_code == 200
        booking_info = res.json()
        assert booking_info.get('booking') == data

    @pytest.mark.skip(reason="Тест ломается, потмоу что нельзя передать другое значение"
                             "кроме Boolean")
    @pytest.mark.parametrize('value', [1, 'sdsdds'])
    def test_invalid_depositpaid_create_booking(self, client, value):
        data = BookingData().random()
        setattr(data, 'depositpaid', value)
        res = client.create_booking(data)
        assert res.status_code == 200
        booking_info = res.json()
        assert booking_info.get('booking') == data

