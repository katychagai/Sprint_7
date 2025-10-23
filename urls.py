
import requests
from .config import get_settings

def base_url():
    return get_settings().base_url.rstrip("/")

def create_courier(payload):
    return requests.post(f"{base_url()}/api/v1/courier", json=payload)

def login_courier(login, password):
    return requests.post(
        f"{base_url()}/api/v1/courier/login", json={"login": login, "password": password}
    )

def login_courier_with_payload(payload):
    return requests.post(f"{base_url()}/api/v1/courier/login", json=payload)

def delete_courier(courier_id):
    return requests.delete(f"{base_url()}/api/v1/courier/{courier_id}")

def create_order(payload):
    return requests.post(f"{base_url()}/api/v1/orders", json=payload)


def list_orders(params=None):
    return requests.get(f"{base_url()}/api/v1/orders", params=params or {})
