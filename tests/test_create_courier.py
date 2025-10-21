import pytest
import allure

from Sprint_7.helpers import generate_courier_data
from Sprint_7.data import MISSING_REQUIRED_FIELDS, DUPLICATE_LOGIN_MESSAGES, STATUS_CREATED, STATUS_DUPLICATE, STATUS_MISSING, MISSING_FIELDS_FOR_CREATE_COURIER
from Sprint_7.urls import create_courier

@allure.epic("Scooter API")
@allure.feature("Courier")
class TestCourierCreate:
    
    @allure.story("Create courier")
    @allure.title("Курьер создается - 201 ok=true")
    def test_courier_can_be_created(self):
        courier_data = generate_courier_data()
        with allure.step("Отправляем запрос на создание курьера"):
            resp = create_courier(courier_data)
            allure.attach(str(resp.json()), "response.json", allure.attachment_type.JSON)
        with allure.step("Проверяем код ответа 201 и тело ответа ok=true"):
            assert resp.status_code == STATUS_CREATED
            assert resp.json().get("ok") is True
    

    @allure.story("Create courier")
    @allure.title("Нельзя создать двух одинаковых курьеров: 409 и сообщение об ошибке")
    def test_cannot_create_duplicate_courier(self):
        courier_data = generate_courier_data()
        with allure.step("Создаем первого курьера"):
            first_resp = create_courier(courier_data)
            assert first_resp.status_code == STATUS_CREATED
            duplicate = {
                "login": courier_data["login"],
                "password": courier_data["password"],
                "firstName": courier_data["firstName"],
            }
        with allure.step("Пытаемся создать курьера с существующим логином"):
            resp = create_courier(duplicate)
            allure.attach(str(resp.json()), "response.json", allure.attachment_type.JSON)
        with allure.step("Проверяем, что вернулся 409 и корректное сообщение"):
            assert resp.status_code == STATUS_DUPLICATE
            assert resp.json().get("message") in DUPLICATE_LOGIN_MESSAGES
       

    @allure.story("Create courier")
    @pytest.mark.parametrize("missing_field", MISSING_REQUIRED_FIELDS)
    def test_missing_required_field_returns_error(self, missing_field):
        allure.dynamic.title(f"Ошибка при отсутствии обязательного поля: {missing_field}")
        payload = generate_courier_data()
        payload.pop(missing_field)
        with allure.step(f"Отправляем запрос без поля {missing_field}"):
            resp = create_courier(payload)
            allure.attach(str(resp.json()), "response.json", allure.attachment_type.JSON)
        with allure.step("Проверяем 400 и сообщение об ошибке"):
            assert resp.status_code == STATUS_MISSING 
            assert resp.json().get("message") == MISSING_FIELDS_FOR_CREATE_COURIER

    @allure.story("Create courier")
    @allure.title("Отсутствие firstName допустимо: 201 и ok=true")
    def test_missing_first_name_is_allowed(self):
        payload = generate_courier_data()
        payload.pop("firstName")
        with allure.step("Отправляем запрос без firstName"):
            resp = create_courier(payload)
            allure.attach(str(resp.json()), "response.json", allure.attachment_type.JSON)
        with allure.step("Проверяем 201 и ok=true"):
            assert resp.status_code == STATUS_CREATED
            assert resp.json().get("ok") is True

