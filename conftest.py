import pytest

from .helpers import generate_order_payload


@pytest.fixture
def order_payload():
    def _factory(colors=None):
        return generate_order_payload(colors)
    return _factory


