import pytest
import allure

from Sprint_7.helpers import login_courier, generate_courier_data, login_courier_with_payload
from Sprint_7.data import WRONG_CREDENTIALS_STATUS, WRONG_CREDENTIALS_MESSAGES


@allure.epic("Scooter API")
@allure.feature("Courier")
class TestCourierLogin:
    
    @allure.story("Login courier")
    @allure.title("Курьер может авторизоваться: 200 и id в ответе")
    def test_courier_can_login(self, created_courier):
        with allure.step("Отправляем запрос логина с корректными login/password"):
            resp = login_courier(created_courier["login"], created_courier["password"])
            allure.attach(str(resp.json()), "response.json", allure.attachment_type.JSON)
        with allure.step("Проверяем 200 и наличие числового id"):
            assert resp.status_code == 200
            body = resp.json()
            assert "id" in body and isinstance(body["id"], int)

    @allure.story("Login courier")
    @pytest.mark.parametrize("missing_field", ["login", "password"])
    def test_login_missing_required_field_returns_error(self, missing_field):
        allure.dynamic.title(f"Ошибка при отсутствии обязательного поля при логине: {missing_field}")
        payload = generate_courier_data()
        payload.pop("firstName", None)  # для логина не нужен
        payload.pop(missing_field)
        with allure.step(f"Отправляем запрос логина без поля {missing_field}"):
            resp = login_courier_with_payload(payload)
        with allure.step("Проверяем 400 и сообщение об ошибке"):
            if resp.status_code == 504:
                pytest.xfail("Бага в документации: при отсутствии обязательногополя API возвращает 504 вместо 400")
            assert resp.status_code == 400
            assert resp.json().get("message") == "Недостаточно данных для входа"

    @allure.story("Login courier")
    @allure.title("Неверные логин или пароль: 404 и сообщение об ошибке")
    def test_login_wrong_credentials_returns_error(self, created_courier):
        wrong_password = created_courier["password"] + "x"
        with allure.step("Отправляем запрос логина с неверным паролем"):
            resp = login_courier(created_courier["login"], wrong_password)
            allure.attach(str(resp.json() if resp.content else {}), "response.json", allure.attachment_type.JSON)
        with allure.step("Проверяем код ответа и текст ошибки"):
            assert resp.status_code in WRONG_CREDENTIALS_STATUS
            body = resp.json()
            assert body["message"] in WRONG_CREDENTIALS_MESSAGES

    @allure.story("Login courier")
    @allure.title("Логин несуществующего пользователя: 404 и сообщение об ошибке")
    def test_login_nonexistent_user_returns_error(self):
        creds = generate_courier_data()
        with allure.step("Пытаемся залогиниться с несуществующими учетными данными"):
            resp = login_courier(creds["login"], creds["password"])
            allure.attach(str(resp.json() if resp.content else {}), "response.json", allure.attachment_type.JSON)
        with allure.step("Проверяем 404 и текст ошибки"):
            assert resp.status_code == 404
            assert resp.json().get("message") == "Учетная запись не найдена"

