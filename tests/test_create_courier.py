import pytest
import allure

from Sprint_7.helpers import create_courier, generate_courier_data, login_courier
from Sprint_7.data import MISSING_REQUIRED_FIELDS, DUPLICATE_LOGIN_MESSAGES


@allure.epic("Scooter API")
@allure.feature("Courier")
class TestCreateCourier:
    
    @allure.story("Create courier")
    @allure.title("Курьер создается и может залогиниться: 201 ok=true; login 200 c id")
    def test_courier_can_be_created(self, created_courier_with_response):
        courier_data, response = created_courier_with_response
        with allure.step("Проверяем код ответа 201 и тело ответа ok=true"):
            assert response.status_code == 201 
            assert response.json().get("ok") is True
        with allure.step("Логинимся с login/password созданного курьера"):
            login_resp = login_courier(courier_data["login"], courier_data["password"])
            allure.attach(str(login_resp.json()), "login_response.json", allure.attachment_type.JSON)
            assert login_resp.status_code == 200
            body = login_resp.json()
            assert "id" in body and isinstance(body["id"], int)

    @allure.story("Create courier")
    @allure.title("Нельзя создать двух одинаковых курьеров: 409 и сообщение об ошибке")
    def test_cannot_create_duplicate_courier(self, created_courier):
        duplicate = {
            "login": created_courier["login"],
            "password": created_courier["password"],
            "firstName": created_courier["firstName"],
        }
        with allure.step("Пытаемся создать курьера с существующим логином"):
            resp = create_courier(duplicate)
            allure.attach(str(resp.json()), "response.json", allure.attachment_type.JSON)
        with allure.step("Проверяем, что вернулся 409 и корректное сообщение"):
            assert resp.status_code == 409
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
            assert resp.status_code == 400 
            assert resp.json().get("message") == "Недостаточно данных для создания учетной записи"

    @allure.story("Create courier")
    @allure.title("Отсутствие firstName допустимо: 201 и ok=true")
    def test_missing_first_name_is_allowed(self, courier_data):
        payload = dict(courier_data)
        payload.pop("firstName")
        with allure.step("Отправляем запрос без firstName"):
            resp = create_courier(payload)
            allure.attach(str(resp.json()), "response.json", allure.attachment_type.JSON)
        with allure.step("Проверяем 201 и ok=true"):
            assert resp.status_code == 201
            assert resp.json().get("ok") is True

    @allure.story("Create courier")
    @allure.title("Структура успешного ответа содержит ok=true")
    def test_success_response_structure(self, created_courier_with_response):
        _, resp = created_courier_with_response
        with allure.step("Проверяем, что в ответе содержится ok=true"):
            allure.attach(str(resp.json()), "response.json", allure.attachment_type.JSON)
            assert resp.json().get("ok") is True

    @allure.story("Create courier")
    @allure.title("Код ответа при создании — 201")
    def test_returns_correct_status_code_on_create(self, created_courier_with_response):
        _, resp = created_courier_with_response
        with allure.step("Код ответа — 201"):
            assert resp.status_code == 201

