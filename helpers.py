import random
import string
import requests
from .config import get_settings


def _base_url():
    return get_settings().base_url.rstrip("/")

def generate_random_string(length=10):
    letters = string.ascii_lowercase
    return "".join(random.choice(letters) for _ in range(length))

def generate_courier_data():
    return {
        "login": generate_random_string(12),
        "password": generate_random_string(12),
        "firstName": generate_random_string(8),
    }

def create_courier(payload):
    return requests.post(f"{_base_url()}/api/v1/courier", json=payload)

def login_courier(login, password):
    return requests.post(
        f"{_base_url()}/api/v1/courier/login", json={"login": login, "password": password}
    )

def get_courier_id(login, password):
    resp = login_courier(login, password)
    if resp.status_code == 200:
        body = resp.json()
        return body.get("id")
    return None

def login_courier_with_payload(payload):
    return requests.post(f"{_base_url()}/api/v1/courier/login", json=payload)

def delete_courier(courier_id):
    return requests.delete(f"{_base_url()}/api/v1/courier/{courier_id}")

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

def create_order(payload):
    return requests.post(f"{_base_url()}/api/v1/orders", json=payload)


def list_orders(params=None):
    return requests.get(f"{_base_url()}/api/v1/orders", params=params or {})


