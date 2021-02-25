from model.booking import BookingData


class TestBooking:

    def test_get_booking(self, client, create_booking):
        """
           1. Add new booking
           2. Get created booking by id
           3. Check data and status
           4. Validate schema
        """
        id_booking = create_booking.get('bookingid')
        res = client.get_booking(id_booking)
        assert res.json() == create_booking.get('booking')

    def test_invalid_get_booking(self, client, create_booking):
        """
           1. Add new booking
           2. Get created booking by id
           3. Check data and status
           4. Validate schema
        """
        res = client.get_booking(1212121212121221)
        assert res.status_code == 404

