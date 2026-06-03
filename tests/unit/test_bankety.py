
import time

from src.steaks_funk import *

import pytest
import allure

@pytest.mark.slow
@allure.epic('тестирую вкладку "Банкеты" ')
@allure.story('UI-проверка корректности данных на вкладке банкеты и валидация ключевой текстовой информации')
def test_banquets_page_content(auth_valid_start):
    launch = auth_valid_start('borzoy_33@mail.ru', 'streaky098')
    with allure.step(f'кликаю на вкладку "Банкеты"'):
        time.sleep(1)
        toClick(launch,By.LINK_TEXT,'Банкеты')
        assert launch.find_element(By.TAG_NAME,"h1").text=="Банкеты"
    with allure.step('проверяю наличие текста промокод и телефон'):
        page_source=launch.page_source
        assert "Праздник - 30" in page_source, "Промокод на скидку не найден на странице!"
        assert "+7(985)612-92-06" in page_source, "Контактный телефон менеджера не найден!"
        assert "Алькасар" in page_source, "Зал 'Алькасар' не найден на странице!"
        assert "Прованс" in page_source, "Зал 'Прованс' не найден на странице!"
        assert "/pages/bankety" in launch.current_url
    with allure.step('проверяю что отображается хотя бы одна фотография'):
        provance_photo=launch.find_element(By.CSS_SELECTOR,"img[src='userfiles/st022.jpg']")
        assert provance_photo.is_displayed(), "Фотография зала Прованс не отображается!"
        assert provance_photo.get_attribute("src")!= " ", "У фотографии отсутствует ссылка на источник!"













