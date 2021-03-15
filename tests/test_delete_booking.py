
class TestDeleteBooking:

    def test_delete_booking(self, client, create_booking):
        """
           1. Add new booking
           2. Get created booking by id
           3. Check data and status
           4. Validate schema
        """
        id_booking = create_booking.get('bookingid')
        res = client.delete_booking(id_booking)
        assert res.status_code == 201

    # def test_delete_invalid_booking(self, client):
    #     """
    #        1. Add new booking
    #        2. Get created booking by id
    #        3. Check data and status
    #        4. Validate schema
    #     """
    #     # id_booking = create_booking.get('bookingid')
    #     res = client.delete_booking(12132231213213231123213)
    #     assert res.status_code == 405