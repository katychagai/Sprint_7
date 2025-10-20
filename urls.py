
import requests
from .helpers import _base_url

def create_courier(payload):
    return requests.post(f"{_base_url()}/api/v1/courier", json=payload)

def login_courier(login, password):
    return requests.post(
        f"{_base_url()}/api/v1/courier/login", json={"login": login, "password": password}
    )

def login_courier_with_payload(payload):
    return requests.post(f"{_base_url()}/api/v1/courier/login", json=payload)

def delete_courier(courier_id):
    return requests.delete(f"{_base_url()}/api/v1/courier/{courier_id}")

def create_order(payload):
    return requests.post(f"{_base_url()}/api/v1/orders", json=payload)


def list_orders(params=None):
    return requests.get(f"{_base_url()}/api/v1/orders", params=params or {})
