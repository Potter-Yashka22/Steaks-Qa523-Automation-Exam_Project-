from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.firefox.options import Options
from selenium.common import TimeoutException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select
import os
import time

def toFind(driver,by,item):
    print(f'ищу элемент {item}')
    r1=WebDriverWait(driver,10).until(
        EC.visibility_of_element_located((by,item))
    )
    print(f'нашёл элемент {item}')
    try:
        driver.execute_script("arguments[0].scrollIntoView({block: 'center','inline: 'center'});",r1)
    except:
        print('прокрутка не отработала')
    return r1

def toClick(driver,by,item):
    element=toFind(driver,by,item)
    print(f'проверка на клик {item}')
    r1 = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((element))
    )
    r1.click()
    print(f'кликнул на элемент {item}')
    return True

def toSend(driver,by,item,text):
    r1=toFind(driver,by,item)
    r1.send_keys(text)
    r1.send_keys(Keys.ENTER)
    print(f'вписал текст в {item}')
    try:
        t1=r1.get_attribute('value')
        print(f'текст виден {t1}')
    except:
        print('теста неть')
    return True

def toSendNoTyping(driver,by,item,text):
    r1=toFind(driver,by,item)
    r1.send_keys(text)
    r1.send_keys(Keys.TAB)
    # r1.send_keys(Keys.ENTER)
    print(f'вписал текст в {item}')
    try:
        t1=r1.get_attribute('value')
        print(f'текст виден {t1}')
    except:
        print('текста нет')
    return True


def getScreen(driver,num):
    time.sleep(2)
    current_dir=os.path.dirname(os.path.abspath(__file__))
    project_root=os.path.dirname(current_dir)
    screenshot_path=os.path.join(project_root,"assets",f"{num}.png")
    driver.save_screenshot(screenshot_path)
    print(f"сделал скриншот: {num}.png в папку assets")
    return True

def toSelect(driver,by,item,value):
    toFind(driver,by,item)
    print(f'проверка на select {item}')
    r1=WebDriverWait(driver,5).until(
        EC.element_to_be_clickable((by,item))
    )
    Select(r1).select_by_value(value)
    print(f'кликнул на элемент {item}')

def toSelectIndex(driver,by,item,index=1):
    time_drop=toFind(driver,by,item)
    print(f'проверка на select {item}')
    r1=WebDriverWait(driver,5).until(
        EC.presence_of_element_located((by,item))
    )
    Select(r1).select_by_index(index)
    print(f'кликнул на элемент {index} в элементе {item}')
    return True




















