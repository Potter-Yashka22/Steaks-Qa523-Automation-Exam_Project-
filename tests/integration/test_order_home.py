from time import process_time

from src.steaks_funk import *
import pytest
import allure
import time


@pytest.mark.integration
@allure.epic('интеграционный тест: заказ еды домой')
@allure.feature('добавление блюда в корзину:интеграция кнопок каталога и счетчика в шапке сайта')
@allure.story('проверка взаимодействия элементов на сайте при заказе доставки')
def test_order_home1(auth_valid_start):
    launch=auth_valid_start('borzoy_33@mail.ru','streaky098')
    time.sleep(1)
    with allure.step('Перехожу на вкладку "Заказать домой"'):
        toClick(launch, By.LINK_TEXT, 'Заказать домой')
        time.sleep(1)
        assert "/#order" in launch.current_url
        assert getScreen(launch,601)
        time.sleep(2)
        season_menu_header=toFind(launch,By.LINK_TEXT,"Сезонное меню")
        header_text=season_menu_header.text.strip()
        expected_text="Сезонное меню"
        assert header_text==expected_text, f"Ошибка! Ожидался текст '{expected_text}', но получен '{header_text}'"
        print(f"Успешно: перешли на страницу, заголовок '{header_text}' отображается!")
    with allure.step('Добавляем выбранные блюда в корзину через цикл'):
        product_list=["2272", "2276", "2165"]
        for prod_id in product_list:
            button_css=f'div[data-product-id="{prod_id}"] button'
            add_button=toFind(launch,By.CSS_SELECTOR,item=button_css)
            launch.execute_script("arguments[0].scrollIntoView({block: 'center'});",add_button)
            time.sleep(0.5)
            add_button.click()
            time.sleep(1)
            print(f"Товар с ID {prod_id} успешно добавлен в корзину")
            time.sleep(1)
        with allure.step('Проверяем, что корзина заполнилась (сумма не равно 0)'):
            cart_total=toFind(launch,By.CSS_SELECTOR,'span[data-type="totalPrice"]')
            cart_text=cart_total.text.strip()
            assert getScreen(launch,602)
            assert "0 руб." not in cart_text, f"Ошибка! Корзина пуста: {cart_text}"
        with allure.step('Нажимаем кнопку "Оформить заказ" в нижней плашке'):
            btn_order_button=toFind(launch,By.XPATH,"//a[contains(text(), 'Оформить заказ')]")
            btn_order_button.click()
            time.sleep(1)
            assert "/cart" in launch.current_url
            t1=toFind(launch,By.CSS_SELECTOR,"h1.m-b-none.col-xs")
            header_text=t1.text.strip()
            expected_text="Корзина"
            assert header_text==expected_text, f"Ошибка! Ожидали заголовок '{expected_text}', но получили {header_text}"
            assert getScreen(launch,603)
            print("Успешно перешли в корзину")
@pytest.mark.integration
@allure.epic('Интеграционный тест: удаление товаров из корзины')
@allure.feature('удаление из корзины: интеграция кнопки каталога и счетчика в шапке сайта')
@allure.story('Удаление блюда из корзины и уменьшение счетчика')
def test_remove_food_from_cart(launch, auth_valid_start):
    # launch = auth_valid_start
    time.sleep(1)
    with allure.step('Проверяем, что находимся в корзине с добавленными товарами'):
        assert "/cart" in launch.current_url
        cart_total=toFind(launch,By.CSS_SELECTOR,'span[data-type="totalPrice"]')
        assert "0 руб." not in cart_total.text.strip()
        assert getScreen(launch,604)
        time.sleep(1)
        print(f"Предыдущий тест оставил нам корзину с суммой: {cart_total.text.strip()}")
    with allure.step('Удаляем товар из корзины кнопкой "Очистить корзину"'):
        clear_cart_btn=toFind(launch,By.CSS_SELECTOR,"button[data-clear-cart]")
        time.sleep(1)
        clear_cart_btn.click()
        assert getScreen(launch,605)
    with allure.step('В модальном окне проверяем присутствие и нажимаем "OK"'):
        confirm_btn=toFind(launch,By.CSS_SELECTOR,"button.swal2-confirm")
        time.sleep(1.5)
        assert confirm_btn.is_displayed(), "Ошибка! Модальное окно подтверждения очистки корзины не появилось на экране."
        print("Модальное окно подтверждения очистки корзины успешно отобразилось!")
        assert getScreen(launch, 606)
        confirm_btn.click()
        time.sleep(1.5)
    with allure.step('Проверяем, что сумма в корзине снова стала равна "0 руб."'):
        cart_total = toFind(launch, By.CSS_SELECTOR, 'span[data-type="totalPrice"]')
        assert "0 руб." in cart_total.text.strip()
        assert getScreen(launch, 607)
        print("Успешное удаление содержимого из корзины")





















