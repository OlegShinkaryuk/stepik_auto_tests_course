from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import os

link = "https://suninjuly.github.io/file_input.html"

try:
    browser = webdriver.Chrome()
    browser.get(link)

    current_dir = os.path.abspath(os.path.dirname(__file__))
    file_path = os.path.join(current_dir, "file.txt")

    input1 = browser.find_element(By.NAME, "firstname")
    input1.send_keys("Ivan")

    input2 = browser.find_element(By.NAME, "lastname")
    input2.send_keys("Petrov")

    input3 = browser.find_element(By.NAME, "email")
    input3.send_keys("lalala@la.com")

    input4 = browser.find_element(By.NAME, "file")
    input4.send_keys(file_path)

    button = browser.find_element(By.TAG_NAME, "button")
    button.click()

finally:
    # успеваем скопировать код за 30 секунд
    time.sleep(7)
    # закрываем браузер после всех манипуляций
    browser.quit()

# не забываем оставить пустую строку в конце файла
# send_keys(file_path)
