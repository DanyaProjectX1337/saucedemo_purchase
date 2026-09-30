from selenium.webdriver.common.by import By


def test_successful_purchase(browser, base_url):
    """Тест успешной покупки товара в магазине SauceDemo."""
    # 1. Открытие страницы по полученному URL
    browser.get(base_url)

    # 2. Авторизация
    browser.find_element(By.ID, "user-name").send_keys("standard_user")
    browser.find_element(By.ID, "password").send_keys("secret_sauce")
    browser.find_element(By.ID, "login-button").click()

    # 3. Добавление товара в корзину и переход к оформлению
    browser.find_element(By.ID, "add-to-cart-sauce-labs-backpack").click()
    browser.find_element(By.CLASS_NAME, "shopping_cart_link").click()
    browser.find_element(By.ID, "checkout").click()

    # 4. Заполнение персональных данных
    browser.find_element(By.ID, "first-name").send_keys("Иван")
    browser.find_element(By.ID, "last-name").send_keys("Иванов")
    browser.find_element(By.ID, "postal-code").send_keys("101000")
    browser.find_element(By.ID, "continue").click()

    # 5. Завершение заказа
    browser.find_element(By.ID, "finish").click()

    # 6. Проверка успешности теста
    confirmation_header = browser.find_element(By.CLASS_NAME, "complete-header")
    assert confirmation_header.text == "Thank you for your order!", (
        f"Ожидался текст 'Thank you for your order!', фактически получен: '{confirmation_header.text}'"
    )