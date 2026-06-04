import time

from src.steaks_funk import *

import allure
import pytest



@pytest.mark.slow
@allure.epic('тестирую личный кабинет')
@allure.feature('функциональная проверка кнопок в ЛК')
@allure.story('проверка кнопок ЛК и актуальной информации о заказе')
@pytest.mark.parametrize("value,screen,expected_text",[
                            ("История заказов",302,"Статус"),
                            ("Купленные товары",303,"Список купленных товаров пуст"),
                            ("Общая информация",304,"Общая информация"),
                            ("Адресная книга",305,"Адресная книга"),
                            ("Смена пароля",306,"Введите новый пароль.")
])
def test_to_private_office(auth_valid_start,value,screen,expected_text):
    launch=auth_valid_start('borzoy_33@mail.ru','streaky098')
    launch.get("https://steiks.ru")
    time.sleep(2)
    with allure.step('кликаю на кнопку "Мой ЛК"'):
        my_acc=toFind(launch,By.CSS_SELECTOR,'a[href="https://steiks.ru/myaccount"]')
        launch.execute_script("arguments[0].click();",my_acc)
        time.sleep(3)
        cabinet_title=toFind(launch,By.CSS_SELECTOR,'h1.main-title')
        assert cabinet_title.text.strip()=="Личный кабинет", f"Ошибка! Ожидали заголовок 'Личный кабинет', но получили '{cabinet_title.text}'"
    with allure.step(f'кликаю на вкладку "{value}"'):
        toClick(launch,By.LINK_TEXT,value)
    with allure.step(f'проверяю что отображается текст: "{expected_text}'):
        time.sleep(1)
        main_content=toFind(launch,By.TAG_NAME,'main')
        assert expected_text in main_content.text,f"текст '{expected_text}' не найден на странице!"
    assert "/myaccount" in launch.current_url
    assert getScreen(launch, num=screen)
    launch.delete_all_cookies()























