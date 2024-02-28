from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math


link = "https://suninjuly.github.io/alert_accept.html"


def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))


try:
    browser = webdriver.Chrome()
    browser.get(link)

    button = browser.find_element(By.TAG_NAME, "button")
    button.click()

    alert = browser.switch_to.alert
    alert.accept()

    x_element = browser.find_element(By.ID, "input_value")
    x = x_element.text
    y = calc(x)

    input1 = browser.find_element(By.TAG_NAME, "input")
    input1.send_keys(str(y))

    button = browser.find_element(By.TAG_NAME, "button")
    button.click()


finally:
    # успеваем скопировать код за 30 секунд
    time.sleep(7)
    # закрываем браузер после всех манипуляций
    browser.quit()

# не забываем оставить пустую строку в конце файла
# send_keys(file_path)
