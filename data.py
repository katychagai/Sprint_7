import pytest

# Обязательные поля для создания курьера
MISSING_REQUIRED_FIELDS = [
    "login",
    "password",
]

# Возможные сообщения при попытке создать дубликат логина
DUPLICATE_LOGIN_MESSAGES = [
    "Этот логин уже используется",
    "Этот логин уже используется. Попробуйте другой.",
]

# Допустимые варианты ответа при неверной паре логин/пароль
WRONG_CREDENTIALS_STATUS = [404, 400]
WRONG_CREDENTIALS_MESSAGES = [
    "Учетная запись не найдена",
    "Недостаточно данных для входа",
    "Неверный логин или пароль",
]

# Параметризация цветов заказа
ORDER_COLORS = [
    pytest.param(["BLACK"], id="BLACK"),
    pytest.param(["GREY"], id="GREY"),
    pytest.param(["BLACK", "GREY"], id="BOTH"),
    pytest.param(None, id="NO_COLOR"),
]


