
import time

import allure


from src.steaks_funk import *
import pytest




@pytest.mark.integration
@allure.epic('интеграционный тест формы бронирования стола')
@allure.feature('тестирую формы и поля при бронирование стола')
@allure.story('проверка заполнения полей и работы функциональных кнопок при резервировании стола')
def test_reserve_a_table(auth_valid_start):
    launch=auth_valid_start('borzoy_33@mail.ru','streaky098')
    time.sleep(1)
    with allure.step('Перехожу на вкладку "Забронировать стол"'):
        toClick(launch,By.LINK_TEXT,'Забронировать стол')
        time.sleep(1)
        assert "/bookingtables" in launch.current_url
        t1=toFind(launch,By.CSS_SELECTOR,'h1.main-title')
        title_text=t1.text
        assert title_text=="Бронирование стола", f"Ожидался текст 'Бронирование стола, получен '{title_text}'"
        assert getScreen(launch,501)
        print(f"Заголовок страницы: {title_text}")
    with allure.step('Выбираем дату бронирования стола'):
        booking_date_input=toFind(launch,By.ID,"btDate")
        launch.execute_script("arguments[0].click();",booking_date_input)
        time.sleep(0.5)
        today_button=toFind(launch,By.CSS_SELECTOR,".flatpickr-day.today")
        launch.execute_script("arguments[0].click();",today_button)
        time.sleep(0.5)
        current_date_val=booking_date_input.get_attribute("value")
        assert booking_date_input.get_attribute("value")!=" ", "Ошибка! Поле даты осталось пустым!"
        assert current_date_val!=" ", "Ошибка! Дата бронирования осталась пустой!"
        print(f"Выбранная дата бронирования: {current_date_val}")
    with allure.step("Выбираем поле 'Время с..'"):
        time_from_input=toFind(launch,By.ID,"btTimeFrom")
        launch.execute_script("arguments[0].click();",time_from_input)
        time.sleep(0.5)
        assert time_from_input.get_attribute("value")!= " ", "Ошибка! Поле 'Время с..' пустое!"
        print(f"Дефолтное время в поле:  {time_from_input.get_attribute('value')}")
    with allure.step('Выбираем количеств гостей'):
        people_count_field=toFind(launch,By.CSS_SELECTOR,'input.spinbox-input[type="number"]')
        current_value=people_count_field.get_attribute("value")
        print(f"Текущее количество: {current_value}")
        plus_button=toFind(launch,By.CSS_SELECTOR,"a.spinbox-more")
        plus_button.click()
        time.sleep(0.5)
        people_count_field=toFind(launch,By.CSS_SELECTOR,'input.spinbox-input[type="number"]')
        new_value=people_count_field.get_attribute("value")
        assert new_value=="2", f"Ожидалось 2, получено: {new_value}"
        print(f"Кол-во гостей изменено на: {new_value}")
    with allure.step('Заполняем комментарий к бронированию'):
        comment_field=toFind(launch,By.ID,"btComment")
        launch.execute_script("arguments[0].scrollIntoView({block: 'center'});",comment_field)
        time.sleep(0.5)
        comment_text="Тестовое бронирование для экзамена QA."
        comment_field.send_keys(comment_text)
        time.sleep(0.5)
        entered_text=comment_field.get_attribute("value")
        assert entered_text==comment_text, f"Ожидался '{comment_text}', получен '{entered_text}'"
        assert getScreen(launch,502)
        print(f"Комментарий добавлен: {entered_text[:50]}...")
    with allure.step('Нажимаем кнопку "Зарезервировать"'):
        reserve_button=toFind(launch,By.CSS_SELECTOR,"button.btn.btn-submit.btn-middle.ladda-button")
        time.sleep(0.5)
        reserve_button.click()
        time.sleep(3)
        success_label=toFind(launch,By.CSS_SELECTOR,"label.form-field-name.vertical-interval-middle")
        entered_text=success_label.text.strip()
        expected_text="Стол забронирован!"
        assert entered_text==expected_text, f"Ожидался текст '{expected_text}', получен '{entered_text}'"
        assert "/bookingtables" in launch.current_url or "booking" in launch.current_url, (f"Не удалось забронировать."
                                                                                    f"Текущий URL: {launch.current_url}")
        print("Бронирование успешно создано")
        assert getScreen(launch,503)


















