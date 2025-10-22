import pytest

from .helpers import generate_order_payload, get_courier_id
from .urls import delete_courier


@pytest.fixture(scope="function")
def courier_cleanup():
    created_couriers = []
    def add_courier_for_cleanup(courier_data):
        created_couriers.append(courier_data)
    
    yield add_courier_for_cleanup
    
    for courier_data in created_couriers:
        courier_id = get_courier_id(courier_data["login"], courier_data["password"])
        delete_courier(courier_id)

@pytest.fixture
def order_payload():
    def create_order_payload(colors=None):
        return generate_order_payload(colors)
    return create_order_payload


