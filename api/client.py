import logging

import requests
import cattr
from common.logs import log
from model.booking import BookingData
from model.login import UserData
from api.booking.booking_api import BookingApi

logger = logging.getLogger()


class Client:
    s = requests.Session()

    def __init__(self, url):
        self.url = url
        self.booking = BookingApi(self)

    @log("Login")
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

    @log("Create booking")
    def create_booking(self, data, type_response):
        data = data.to_dict()
        response = self.s.post(self.url + "/booking", json=data)
        response.data = cattr.structure(response.json(), type_response)
        return response

    def update_booking(self, uid: int, data: BookingData):
        data = data.object_to_dict()
        return self.s.put(self.url + f"/booking/{uid}", json=data)

    def delete_booking(self, uid: int):
        return self.s.delete(self.url + f"/booking/{uid}")

    @log("Delete booking")
    def get_booking(self, uid: int):
        return self.s.get(self.url + f"/booking/{uid}")

