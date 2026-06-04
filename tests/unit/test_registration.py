import time

from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from src.steaks_funk import *
import allure
import pytest


@pytest.mark.high
@allure.epic('тестирую регистрацию на сайте https://steiks.ru/')
@allure.feature('Регистрация: обязательные поля')
@allure.story('Проверка перехода на форму регистрации')
def test_registration(launch):
    fake_email="tqujeqwijxvpeho-23138@furvionx.com"
    email_field=toFind(launch,By.ID,"email")
    email_field.send_keys(fake_email)
    cont_btn=toFind(launch,By.CSS_SELECTOR,'button[type="submit"]')
    cont_btn.click()
    time.sleep(1.5)
    with allure.step('проверяю в заголовке наличие слова "Регистрация"'):
        reg_title=toFind(launch,By.CSS_SELECTOR,'.login-header__title')
        header_text=reg_title.text.strip()
        assert "Регистрация" in header_text, f"Ошибка! Ожидали заголовок 'Регистрация', но получили '{header_text}'"
@pytest.mark.high
@allure.feature('Регистрация: обязательные поля')
@allure.story('Проверка значения required у поля FirstName')
def test_reg_type1(launch):
    t1=toFind(launch,By.CSS_SELECTOR,'input[data-ng-model="$ctrl.registration.FirstName"]')
    toSendNoTyping(launch,By.CSS_SELECTOR,'input[data-ng-model="$ctrl.registration.FirstName"]','Геннадий')
    time.sleep(1.5)
    with allure.step('Проверяю наличие значения required пр заполнении поля FirstName'):
        assert t1.get_attribute('required') is not None
    with allure.step('Делаю скриншот'):
        assert getScreen(launch,100)
@pytest.mark.high
@allure.feature('Регистрация: обязательные поля')
@allure.story('Проверка значения required у поля LastName')
def test_reg_type2(launch):
    t2=toFind(launch,By.CSS_SELECTOR,'input[data-ng-model="$ctrl.registration.LastName"]')
    toSendNoTyping(launch,By.CSS_SELECTOR,'input[data-ng-model="$ctrl.registration.LastName"]','Крапивцев')
    time.sleep(1)
    with allure.step('Проверяю наличие значения required пр заполнении поля LastName'):
        assert t2.get_attribute('required') is not None
    with allure.step('Делаю скриншот'):
        assert getScreen(launch,101)
@pytest.mark.high
@allure.feature('Регистрация: обязательные поля')
@allure.story('Проверка значения required у поля Phone')
def test_reg_type4(launch):
    phone_field=toFind(launch,By.CSS_SELECTOR,"input[type='tel']")
    phone_field.click()
    phone_field.send_keys(Keys.CONTROL +"a")
    phone_field.send_keys(Keys.BACKSPACE)
    time.sleep(0.5)
    my_phone_numb="9209216548"
    for digit in my_phone_numb:
        phone_field.send_keys(digit)
        time.sleep(2)
    with allure.step('Проверяю наличие значения required пр заполнении поля Phone'):
        assert phone_field.get_attribute('required') is not None
    with allure.step('Делаю скриншот'):
        assert getScreen(launch,103)
@pytest.mark.high
@allure.feature('Регистрация: обязательные поля')
@allure.story('Проверка значения required у поля Password')
def test_reg_type5(launch):
    pass_field=toFind(launch,By.CSS_SELECTOR,'input[data-ng-model="$ctrl.registration.Password"]')
    pass_field.click()
    toSendNoTyping(launch,By.CSS_SELECTOR,'input[data-ng-model="$ctrl.registration.Password"]','pythonpath479')
    t1=toFind(launch,By.CSS_SELECTOR,'input[data-ng-model="$ctrl.registration.Password"]')
    with allure.step('Проверяю наличие значения required пр заполнении поля Password'):
        assert t1.get_attribute('required') is not None
    with allure.step('Делаю скриншот'):
        assert getScreen(launch,104)
@pytest.mark.high
@allure.feature('Регистрация: обязательные поля')
@allure.story('Проверка значения required у поля PasswordConfirm')
def test_reg_type6(launch):
    confirm_pass=toFind(launch,By.CSS_SELECTOR,'input[data-ng-model="$ctrl.registration.PasswordConfirm"]')
    confirm_pass.click()
    toSendNoTyping(launch,By.CSS_SELECTOR,'input[data-ng-model="$ctrl.registration.PasswordConfirm"]','pythonpath479')
    t1=toFind(launch,By.CSS_SELECTOR,'input[data-ng-model="$ctrl.registration.PasswordConfirm"]')
    time.sleep(4)
    with allure.step('Проверяю наличие значения required пр заполнении поля PasswordConfirm'):
        assert t1.get_attribute('required') is not None
    with allure.step('Делаю скриншот'):
        assert getScreen(launch,105)
@pytest.mark.high
@allure.feature('Регистрация: обязательные поля')
@allure.story('Проверка перехода на следующую страницу после регистрации')
def test_reg_type7(launch):
    with allure.step('РУЧНОЙ ВВОД КАПЧИ: Пауза 30 секунд'):
        time.sleep(30)
        # завешиваю драйвер чтобы руками заполнить капчу
        toClick(launch,By.CSS_SELECTOR,'button.btn-submit.registration-action')
        time.sleep(4)
    with allure.step('Проверяю что URL после нажатия кнопки "Регистрация" изменился'):
        assert "https://steiks.ru/" in launch.current_url
    time.sleep(15)
    t1 = toFind(launch, By.CSS_SELECTOR,'a[href="https://steiks.ru/myaccount"]')
    with allure.step('Проверяю что появилась кнопка "Мой ЛК" после успешной регистрации'):
        assert "Мой ЛК" in t1.text
    with allure.step('Делаю скриншот'):
        assert getScreen(launch,106)













