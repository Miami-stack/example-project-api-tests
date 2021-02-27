import logging

import requests
from schema import Schema, And


from model.booking import BookingData
from model.login import UserData
from api.booking.booking_api import BookingApi

logger = logging.getLogger()


class Client:
    s = requests.Session()

    def __init__(self, url):
        self.url = url
        self.booking = BookingApi(self)

    def login(self, user_data: UserData):
        data = user_data.__dict__
        return self.s.post(self.url + "/auth", json=data)

    def authorize(self, user_data: UserData):
        res = self.login(user_data)
        if res.status_code != 200:
            raise Exception("Error to authorize")
        session_token = res.json().get("token")
        logger.info(f'Get token {session_token}')
        cookie = requests.cookies.create_cookie("token", session_token)
        self.s.cookies.set_cookie(cookie)

    def create_booking(self, data: BookingData):
        data = data.object_to_dict()
        return self.s.post(self.url + "/booking", json=data)

    def update_booking(self, uid: int, data: BookingData):
        data = data.object_to_dict()
        return self.s.put(self.url + f"/booking/{uid}", json=data)

    def get_booking(self, uid: int):
        return self.s.get(self.url + f"/booking/{uid}")

