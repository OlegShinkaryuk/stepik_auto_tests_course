import math

from selenium import webdriver
from selenium.webdriver.common.by import By
import time


def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))


link = "https://suninjuly.github.io/get_attribute.html"

try:
    browser = webdriver.Chrome()
    browser.get(link)

    x_element_to_find = browser.find_element(By.ID, "treasure")
    x_element = x_element_to_find.get_attribute("valuex")
    print(x_element)

    y = calc(x_element)

    input1 = browser.find_element(By.TAG_NAME, "input")
    input1.send_keys(str(y))

    option1 = browser.find_element(By.ID, "robotCheckbox")
    option1.click()

    option2 = browser.find_element(By.ID, "robotsRule")
    option2.click()

    option3 = browser.find_element(By.CSS_SELECTOR, "button")
    option3.click()

finally:
    # успеваем скопировать код за 30 секунд
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()

# не забываем оставить пустую строку в конце файла
