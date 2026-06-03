import time

from src.steaks_funk import *
import allure
import pytest


@pytest.mark.slow
@allure.epic('Проверка смены пароля в ЛК-негативные проверки')
@allure.feature('Проверка ввода некорректных данных при смене пароля')
@allure.story('Проверка ввода пробелов в полях "новый пароль" и "подтвердите пароль"')
@pytest.mark.parametrize("new_password,confirm_password, expected_error",[
    ("  ", "  ", "Неверные данные")
])
def test_private_office_change_password_negative(auth_valid_start,new_password,confirm_password,expected_error):
    launch = auth_valid_start('borzoy_33@mail.ru', 'streaky098')
    with allure.step('Захожу на вкладку Мой ЛК'):
        time.sleep(2)
        lk_button = toFind(launch, By.CSS_SELECTOR, 'a[href*="myaccount"]')
        launch.execute_script("arguments[0].click();", lk_button)
    with allure.step('переходим на вкладку "Смена пароля"'):
        time.sleep(1)
        toClick(launch,By.LINK_TEXT,'Смена пароля')
    with allure.step('заполняем форму пустыми символами(два пробела)'):
        toSend(launch,By.ID,'NewPassword',new_password)
        toSend(launch,By.ID,'NewPasswordConfirm',confirm_password)
        toClick(launch,By.CSS_SELECTOR,"button[data-button-validation-success*='changePassword']")
        with allure.step('Проверяю отображение всплывающей ошибки'):
            WebDriverWait(launch,5).until(
                EC.text_to_be_present_in_element((By.CSS_SELECTOR,".toast-message"),"Неверные данные")
            )
            error_text=toFind(launch, By.CSS_SELECTOR, '.toast-message').text
            assert expected_error in error_text, f" Ожидалась ошибка '{expected_error}', получено '{error_text}'"
        assert getScreen(launch, num=310)

















