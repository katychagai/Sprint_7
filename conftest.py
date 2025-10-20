import pytest

from .helpers import (
    create_courier,
    get_courier_id,
    delete_courier,
    generate_order_payload,
    generate_courier_data
)

@pytest.fixture
def created_courier():
    courier_data = generate_courier_data()  
    resp = create_courier(courier_data)
    yield courier_data, resp
    courier_id = get_courier_id(courier_data["login"], courier_data["password"])
    if courier_id:
        delete_courier(courier_id)

@pytest.fixture
def order_payload():
    def _factory(colors=None):
        return generate_order_payload(colors)
    return _factory


