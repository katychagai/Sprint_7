
import allure

from Sprint_7.urls import list_orders
from Sprint_7.data import STATUS_OK


@allure.epic("Scooter API")
@allure.feature("Orders")
class TestOrdersList:
    
    
    @allure.story("List orders")
    @allure.title("GET /api/v1/orders возвращает список заказов")
    def test_orders_list_contains_orders_array(self):
        with allure.step("Отправляем GET /api/v1/orders"):
            resp = list_orders()
            body = resp.json()
            allure.attach(str(body), "response.json", allure.attachment_type.JSON)
        with allure.step("Проверяем 200 и наличие массива orders"):
            assert resp.status_code == STATUS_OK
            assert "orders" in body and isinstance(body["orders"], list)


