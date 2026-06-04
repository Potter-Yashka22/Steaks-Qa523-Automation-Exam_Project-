import time

from src.steaks_funk import *
import allure
import pytest

from tests.conftest import launch


@pytest.mark.slow
@allure.epic('тестирую добавление подарочных карт в корзину')
@allure.feature('параметризированный e2e тест на добавление подарочных карт в корзину')
@allure.story('проверка входа под валидными логином и паролем')
@pytest.mark.parametrize("card_id, card_name, expected_price,screen",[
                    (2284,"Подарочная карта 3000Р",3000,401),
                    (2285,"Подарочная карта 5000Р",5000,402),
                    (2283,"Подарочная карта 10000Р",10000,403)
])
def test_add_card_to_cart(auth_valid_start,card_id,card_name,expected_price,screen):
    launch=auth_valid_start('borzoy_33@mail.ru','streaky098')
    time.sleep(1)
    with allure.step(f'Переходим на вкладку подарочные карты и добавляем карту {card_name}'):
        toClick(launch,By.LINK_TEXT,'Подарочные карты')
        assert getScreen(launch,404)
        assert '/categories/podarochnye-karty' in launch.current_url
        p_title_e=toFind(launch,By.CSS_SELECTOR,'.catalog-title h1')
        assert p_title_e.text.strip()=="Подарочные карты"
        time.sleep(1)
    with allure.step('Добавляем карту в корзину'):
        card_button_css = f"div[data-product-id='{card_id}'] button[data-ng-switch-when='add']"
        add_button = WebDriverWait(launch, 10).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, card_button_css))
        )
        launch.execute_script("arguments[0].scrollIntoView({block: 'center', behavior: 'smooth'});", add_button)
        time.sleep(2)
        launch.execute_script("arguments[0].click();", add_button)
        assert getScreen(launch,405)
        cart_price_el=WebDriverWait(launch,5).until(
            EC.presence_of_element_located((By.CSS_SELECTOR,"span.cart-mini-main-count--price"))
        )
        current_cart_text=cart_price_el.text
        clean_cart_text = current_cart_text.replace(" ", "").replace("\u00a0", "")
        assert str(expected_price) in clean_cart_text, f"Ошибка! Ожидали {expected_price} но получили {current_cart_text}"
        time.sleep(1)
    with allure.step('Переходим к оформлению через мини-корзину'):
        time.sleep(2)
        assert getScreen(launch,406)
        cart_try=toFind(launch,By.CSS_SELECTOR,"a[data-cart-mini-trigger]")
        launch.execute_script("arguments[0].click();", cart_try)
        time.sleep(1)
        checkout_button = toFind(launch, By.CSS_SELECTOR, "a[href='checkout']")
        launch.execute_script("arguments[0].click();", checkout_button)
        checkout_title = toFind(launch, By.CSS_SELECTOR, "h1.main-title")
        assert '/checkout' in launch.current_url
        assert checkout_title.text.strip() == "Оформление заказа", f"Ожидалось 'Оформление заказа', текущий заголовок:{checkout_title.text}"
        time.sleep(2)
    with allure.step('Заполняем форму оформления заказа (Москва-самовывоз)'):
        time.sleep(2)
        pickup_radio=toFind(launch,By.CSS_SELECTOR,"img[alt='Самовывоз']")
        launch.execute_script("arguments[0].scrollIntoView({block: 'center'});", pickup_radio)
        time.sleep(0.5)
        pickup_radio.click()
        time.sleep(0.5)
        date_field=toFind(launch,By.ID,"DateOfDelivery")
        launch.execute_script("arguments[0].click();",date_field)
        time.sleep(0.5)
        today_btn=toFind(launch,By.CSS_SELECTOR,".flatpickr-day.today")
        launch.execute_script("arguments[0].click();",today_btn)
        assert date_field.get_attribute("value")!=" ", "Ошибка! Дата самовывоза не выбрана в календаре!"
        time_field=toFind(launch,By.CSS_SELECTOR,"select[data-ng-model='shippingList.selectShipping.TimeOfDelivery']")
        assert time_field.is_displayed(), "Ошибка! После выбора даты поле времени не появилось!"
        time.sleep(1)
        toSelectIndex(launch, By.CSS_SELECTOR, 'select[data-ng-model="shippingList.selectShipping.TimeOfDelivery"]', 3)
        assert getScreen(launch, 407)
        time.sleep(1)
    with allure.step('Пишем комментарий к заказу с скроллом'):
        time.sleep(1)
        comment_field=toFind(launch,By.ID,'CustomerComment')
        launch.execute_script("arguments[0].scrollIntoView({block: 'center'});",comment_field)
        time.sleep(1)
        comment_field.clear()
        comment_field.send_keys('Тестовый заказ для экзамена QA.Не готовить.')
        time.sleep(1)
        assert getScreen(launch,408)
        assert comment_field.get_attribute(
            "value") == "Тестовый заказ для экзамена QA.Не готовить.","Ошибка! Комментарий к заказу не ввелся в поле!"
    with allure.step('Заполняем поле "количество приборов"'):
        time.sleep(1)
        eating_utensils=toFind(launch,By.ID,'CountDevices')
        eating_utensils.clear()
        eating_utensils.send_keys('1')
        time.sleep(0.5)
        assert eating_utensils.get_attribute("value")=="1", "Ошибка! Кол-во приборов не равно 1"
        assert getScreen(launch,409)
    with allure.step('Нажимаем кнопку "Оплатить заказ"'):
        time.sleep(1)
        order_button=toFind(launch,By.CSS_SELECTOR,'button[data-e2e="btnCheckout"]')
        launch.execute_script("arguments[0].scrollIntoView({block: 'center'});",order_button)
        time.sleep(1)
        launch.execute_script("arguments[0].click();", order_button)
        time.sleep(2)
        assert "/checkout/success" in launch.current_url, f"Ошибка! Страница оформления заказа не загрузилась!Текущий URL: {launch.current_url}"
        success_text_el=toFind(launch,By.XPATH,"//*[contains(text(), 'Ваш заказ принят под номером')]")
        assert success_text_el.is_displayed(),"Ошибка! Текст с номером заказа не найден!"
    with allure.step('Делаем скриншот'):
        getScreen(launch,f'{screen}')
    with allure.step('Очищаем сессию для следующего теста'):
        launch.get("https://steiks.ru")
        time.sleep(1)
        launch.delete_all_cookies()
        launch.execute_script("window.localStorage.clear();")
        launch.execute_script("window.sessionStorage.clear();")
        time.sleep(2)


















