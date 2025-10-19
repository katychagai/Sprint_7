
import allure

from Sprint_7.helpers import list_orders


@allure.epic("Scooter API")
@allure.feature("Orders")
class TestListOrders:
    
    
    @allure.story("List orders")
    @allure.title("GET /api/v1/orders возвращает список заказов")
    def test_orders_list_contains_orders_array(self):
        with allure.step("Отправляем GET /api/v1/orders"):
            resp = list_orders()
            body = resp.json()
            allure.attach(str(body), "response.json", allure.attachment_type.JSON)
        with allure.step("Проверяем 200 и наличие массива orders"):
            assert resp.status_code == 200
            assert "orders" in body and isinstance(body["orders"], list)


