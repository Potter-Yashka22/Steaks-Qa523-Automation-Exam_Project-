import time

from src.steaks_funk import *
import allure
import pytest


@pytest.mark.slow
@allure.epic('Проверка смены пароля в ЛК-негативные проверки')
@allure.feature('Проверка ввода некорректных данных при смене пароля')
@allure.story('Проверка ввода пробелов в полях "новый пароль" и "подтвердите пароль"')
@pytest.mark.parametrize("new_password,confirm_password, expected_error",[
    ("1", "1", "Длина пароля должна быть не менее 6 символов")
])
def test_private_office_change_password_negative(auth_valid_start,new_password,confirm_password,expected_error):
    launch = auth_valid_start('borzoy_33@mail.ru', 'streaky098')
    with allure.step('Захожу на вкладку Мой ЛК'):
        launch.get("https://steiks.ru/myaccount")
    with allure.step('переходим на вкладку "Смена пароля"'):
        time.sleep(1)
        toClick(launch,By.CSS_SELECTOR,'#changepassword a')
    with allure.step('заполняем формы только по одному символу'):
        toSend(launch,By.ID,'NewPassword',new_password)
        toSend(launch,By.ID,'NewPasswordConfirm',confirm_password)
        toClick(launch,By.CSS_SELECTOR,"button[data-button-validation-success*='changePassword']")
        with allure.step('Проверяю отображение всплывающей ошибки'):
            error_text=toFind(launch,By.CSS_SELECTOR,'.toast-message').text
            assert expected_error in error_text, f"Ожидалась ошибка '{expected_error}', но получено '{error_text}'"
            assert getScreen(launch, num=312)








