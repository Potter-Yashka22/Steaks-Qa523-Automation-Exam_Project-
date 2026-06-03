import time

from src.steaks_funk import *
import allure
import pytest

from tests.conftest import launch


@pytest.mark.slow
@allure.epic('тестирую добавление подарочных карт в корзину')
@allure.feature('параметризированный unit тест на добавление подарочных карт в корзину')
@allure.story('проверка входа под валидными логином и паролем')
@pytest.mark.parametrize("card_id, card_name, expected_price,screen",[
                    (2284,"Подарочная карта 3000Р",3000,201),
                    (2285,"Подарочная карта 5000Р",5000,202),
                    (2283,"Подарочная карта 10000Р",10000,203)
])
def test_add_card_to_cart(auth_valid_start,card_id,card_name,expected_price,screen):
    launch=auth_valid_start('borzoy_33@mail.ru','streaky098')
    with allure.step(f'Добавляем карту {card_name}'):
        toClick(launch,By.LINK_TEXT,'Подарочные карты')
        time.sleep(2)
        card_button_css = f"[data-product-id='{card_id}'] .cart-add__button-add"
        add_button = WebDriverWait(launch, 10).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, card_button_css))
        )
        launch.execute_script("arguments[0].scrollIntoView({block: 'center', behavior: 'smooth'});", add_button)
        time.sleep(1)
        launch.execute_script("arguments[0].click();", add_button)
        time.sleep(1)
    with allure.step('делаю скрин-шот'):
        getScreen(launch,f'{screen}')
    with allure.step('проверяю что корзина не пуста'):
        cart_item=toFind(launch,By.CSS_SELECTOR,'.cart-mini-main-count')
        cart_text=cart_item.text.strip()
        assert cart_text!='0',f'Корзина пуста: {cart_text}'
        assert cart_text!='flex',f"Получен текст 'flex' вместо количества"
        assert cart_text!='', "Счетчик корзины пустой"
    with allure.step('Делаю сброс сессии и очистку куки'):
        launch.delete_all_cookies()
        launch.execute_script("window.localStorage.clear();")
        launch.execute_script("window.sessionStorage.clear();")
        time.sleep(1)


'''
этот шаг нужен в случае если разрабы опять перепишут код и всплывающая корзина
 будет перекрывать кнопки добавления карт
# toClick(launch,By.CSS_SELECTOR,f'[data-offer-id="{offer_id}"] button.cart-add___button-add')
    # with allure.step('Закрываю всплывающее окно корзины'):
    #     time.sleep(1)
    #     close_button=toFind(launch,By.CSS_SELECTOR,'.sidebar__close')
    #     close_button.click()
    #     time.sleep(1)'''






























