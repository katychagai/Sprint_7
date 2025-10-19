import pytest

from .helpers import (
    generate_courier_data,
    create_courier,
    get_courier_id,
    delete_courier,
    generate_order_payload,
)


@pytest.fixture
def courier_data():
    return generate_courier_data()


@pytest.fixture
def created_courier(courier_data):
    response = create_courier(courier_data)
    assert response.status_code == 201
    yield courier_data
    courier_id = get_courier_id(courier_data["login"], courier_data["password"])
    if courier_id is not None:
        delete_courier(courier_id)


@pytest.fixture
def created_courier_with_response(courier_data):
    response = create_courier(courier_data)
    assert response.status_code == 201
    yield courier_data, response
    courier_id = get_courier_id(courier_data["login"], courier_data["password"])
    if courier_id is not None:
        delete_courier(courier_id)


@pytest.fixture
def order_payload():
    def _factory(colors=None):
        return generate_order_payload(colors)
    return _factory


