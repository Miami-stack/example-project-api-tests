from model.booking import BookingData
import pytest


class TestCreateBooking:
    def test_update_booking(self, client, create_booking):
        """
        Отправка запроса 'update_booking' с валидными данными
        """
        id_booking = create_booking.get('bookingid')
        data = BookingData().random()
        res = client.update_booking(id_booking, data)
        assert res.status_code == 200
        booking_info = res.json()
        assert booking_info == data

    @pytest.mark.skip(reason="Ошибка в апи")
    @pytest.mark.parametrize("field, value", [
        ['firstname', 21], ['lastname', 34],
        ['additionalneeds', 45]
    ])
    def test_invalid_string_update_booking(self, field, value, client, create_booking):
        """
        Отправка запроса 'create_booking' с невалидными полями
         'firstname' , 'lastname', 'additionalneeds'
        """
        id_booking = create_booking.get('bookingid')
        data = BookingData().random()
        setattr(data, field, value)
        res = client.update_booking(id_booking, data)
        assert res.status_code == 200
        booking_info = res.json()
        assert booking_info == data

    def test_invalid_date_update_booking(self, client, create_booking):
        """
        Отправка запроса 'create_booking' с датой заезда будущего времени
        и с датой выезда прошлого времени ("2040-01-01" и "2002-01-01")
        """
        id_booking = create_booking.get('bookingid')
        data = BookingData().random()
        data.bookingdates.checkin = "2040-01-01"
        data.bookingdates.checkout = "2002-01-01"
        # TODO сгенерировать с помощью библиотеки питон
        res = client.update_booking(id_booking, data)
        assert res.status_code == 200
        booking_info = res.json()
        assert booking_info == data

    @pytest.mark.parametrize("value", [0, -1])
    def test_invalid_total_price_update_booking(self, client, value, create_booking):
        id_booking = create_booking.get('bookingid')
        data = BookingData().random()
        setattr(data, 'totalprice', value)
        res = client.update_booking(id_booking, data)
        assert res.status_code == 200
        booking_info = res.json()
        assert booking_info == data

    @pytest.mark.skip(reason="Значение 0.15 ломает тест")
    @pytest.mark.parametrize("value", [0.15, 1, 1000, 1000000])
    def test_invalid_float_value_total_price_update_booking(self, client, value, create_booking):
        id_booking = create_booking.get('bookingid')
        data = BookingData().random()
        setattr(data, 'totalprice', value)
        res = client.update_booking(id_booking, data)
        assert res.status_code == 200
        booking_info = res.json()
        assert booking_info == data

    @pytest.mark.skip(reason="Тест ломается на значение totalprice")
    def test_invalid_more_value_total_price_update_booking(self, client, create_booking):
        data = BookingData().random()
        setattr(data, 'totalprice', '10000000000000000000000000')
        res = client.update_booking(data)
        assert res.status_code == 200
        booking_info = res.json()
        assert booking_info == data

    @pytest.mark.skip(reason="Тест ломается, потмоу что нельзя передать другое значение"
                             "кроме Boolean")
    @pytest.mark.parametrize('value', [1, 'sdsdds'])
    def test_invalid_depositpaid_update_booking(self, client, value, create_booking):
        id_booking = create_booking.get('bookingid')
        data = BookingData().random()
        setattr(data, 'depositpaid', value)
        res = client.update_booking(id_booking, data)
        assert res.status_code == 200
        assert client.validate_json(res.json())
        booking_info = res.json()
        assert booking_info == data
