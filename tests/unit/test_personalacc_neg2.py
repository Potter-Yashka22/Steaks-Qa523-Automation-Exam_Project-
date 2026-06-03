import time

from src.steaks_funk import *
import allure
import pytest


@pytest.mark.slow
@allure.epic('Проверка смены пароля в ЛК-негативные проверки')
@allure.feature('Проверка ввода некорректных данных при смене пароля')
@allure.story('Проверка ввода пробелов в полях "новый пароль" и "подтвердите пароль"')
@pytest.mark.parametrize("new_password,confirm_password, expected_error",[
    ("super-pass123","wrong-confirm","Введенные пароли не совпадают")
])
def test_private_office_change_password_negative(auth_valid_start,new_password,confirm_password,expected_error):
    launch = auth_valid_start('borzoy_33@mail.ru', 'streaky098')
    with allure.step('Захожу на вкладку Мой ЛК'):
        launch.get("https://steiks.ru/myaccount")
    with allure.step('переходим на вкладку "Смена пароля"'):
        time.sleep(1)
        toClick(launch,By.LINK_TEXT,'Смена пароля')
    with allure.step('заполняем формы разными паролями'):
        toSend(launch,By.ID,'NewPassword',new_password)
        toSend(launch,By.ID,'NewPasswordConfirm',confirm_password)
        toClick(launch,By.CSS_SELECTOR,"button[data-button-validation-success*='changePassword']")
        with allure.step('Проверяю отображение всплывающей ошибки'):
            WebDriverWait(launch,5).until(
                EC.text_to_be_present_in_element((By.CSS_SELECTOR,".toast-message"),"Введенные пароли не совпадают")
            )
        assert getScreen(launch, num=311)
