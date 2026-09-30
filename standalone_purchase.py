import time
from selenium import webdriver
from selenium.webdriver.common.by import By

# 1. Старт браузера и переход на сайт
driver = webdriver.Chrome()
driver.maximize_window()
driver.implicitly_wait(10)

try:
    driver.get("https://www.saucedemo.com/")

    # 2. Авторизация (standard_user)
    driver.find_element(By.ID, "user-name").send_keys("standard_user")
    driver.find_element(By.ID, "password").send_keys("secret_sauce")
    driver.find_element(By.ID, "login-button").click()

    # 3. Добавление товара в корзину и переход к оформлению
    driver.find_element(By.ID, "add-to-cart-sauce-labs-backpack").click()
    driver.find_element(By.CLASS_NAME, "shopping_cart_link").click()
    driver.find_element(By.ID, "checkout").click()

    # 4. Заполнение формы
    driver.find_element(By.ID, "first-name").send_keys("Иван")
    driver.find_element(By.ID, "last-name").send_keys("Иванов")
    driver.find_element(By.ID, "postal-code").send_keys("101000")
    driver.find_element(By.ID, "continue").click()

    # 5. Покупка товара
    driver.find_element(By.ID, "finish").click()

    # Проверка отображения сообщения
    order_complete_msg = driver.find_element(By.CLASS_NAME, "complete-header").text
    print(f"Статус заказа: {order_complete_msg}")
    time.sleep(2)

finally:
    # 6. Закрытие браузера
    driver.quit()