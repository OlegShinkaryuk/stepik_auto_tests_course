from selenium.webdriver.support.select import Select
from selenium import webdriver
from selenium.webdriver.common.by import By
import time


link = "https://suninjuly.github.io/selects2.html"

try:
    browser = webdriver.Chrome()
    browser.get(link)

    x = browser.find_element(By.ID, "num1").text
    y = browser.find_element(By.ID, "num2").text
    result = int(x) + int(y)

    print(result)

    option = browser.find_element(By.ID, "dropdown").click()
    option = browser.find_element(By.CSS_SELECTOR, f"[value='{result}']").click()

    option3 = browser.find_element(By.CSS_SELECTOR, "button")
    option3.click()

finally:
    # успеваем скопировать код за 30 секунд
    time.sleep(7)
    # закрываем браузер после всех манипуляций
    browser.quit()

# не забываем оставить пустую строку в конце файла
