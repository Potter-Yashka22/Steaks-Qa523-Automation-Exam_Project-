
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from src.steaks_funk import *
import pytest
import time

@pytest.fixture(scope='module')
def launch():
    options=Options()
    # options.add_argument("--headless")
    driver=webdriver.Firefox(options=options)
    driver.set_page_load_timeout(7)
    driver.implicitly_wait(10)
    try:
        driver.get('https://steiks.ru/login')
    except TimeoutException:
        print('Сайт не загружается')
    yield driver
    driver.quit()

@pytest.fixture(scope='module')
def auth_valid_start(launch):
    def _auth(email,password):
        time.sleep(1)
        launch.get("https://steiks.ru/login")
        try:
            email_toggle = launch.find_element(By.XPATH, "//*[contains(text(), 'Войти по email')]")
            email_toggle.click()
            time.sleep(1)
            print("Успешно переключились на форму Email")
        except Exception:
            print("Форма Email уже открыта по умолчанию, пропускаю клик переключения")
        print("Запускаю процесс двухэтапной авторизации...")
        toSend(launch, By.ID, item='email', text=email)
        time.sleep(1)
        toClick(launch, By.CSS_SELECTOR, item='button.login-action')
        WebDriverWait(launch, timeout=8).until(
            EC.element_to_be_clickable((By.ID, 'password'))
        )
        time.sleep(2)
        toSend(launch, By.ID, item='password', text=password)
        toClick(launch, By.CSS_SELECTOR, item='button.login-action')
        print("Авторизация успешно выполнена автотестом!")
        return launch
    return _auth











