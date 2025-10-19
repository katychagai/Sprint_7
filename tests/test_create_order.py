import pytest
import allure

from Sprint_7.helpers import create_order
from Sprint_7.data import ORDER_COLORS


@allure.epic("Scooter API")
@allure.feature("Orders")
class TestCreateOrder:
    
    @allure.story("Create order")
    @pytest.mark.parametrize("colors", ORDER_COLORS)
    def test_create_order_with_various_colors(self, colors, order_payload):
        allure.dynamic.title(f"Создание заказа с color={colors}")
        payload = order_payload(colors)
        with allure.step("Создаем заказ"):
            resp = create_order(payload)
            body = resp.json()
            allure.attach(str(body), "response.json", allure.attachment_type.JSON)
        with allure.step("Проверяем 201 и наличие track"):
            assert resp.status_code == 201
            assert "track" in body and isinstance(body["track"], int)


