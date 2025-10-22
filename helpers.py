import random
import string
from .urls import login_courier

def generate_random_string(length=10):
    letters = string.ascii_lowercase
    return "".join(random.choice(letters) for _ in range(length))

def generate_courier_data():
    return {
        "login": generate_random_string(12),
        "password": generate_random_string(12),
        "firstName": generate_random_string(8),
    }

def get_courier_id(login, password):
    resp = login_courier(login, password)
    if resp.status_code == 200:
        body = resp.json()
        return body.get("id")
    return None

def generate_order_payload(color=None):
    payload = {
        "firstName": generate_random_string(6).title(),
        "lastName": generate_random_string(8).title(),
        "address": "Moscow, Test street, 1",
        "metroStation": 4,
        "phone": "+7 800 355 35 35",
        "rentTime": 5,
        "deliveryDate": "2025-10-20",
        "comment": "Autotest order",
    }
    if color is not None:
        payload["color"] = color
    return payload


