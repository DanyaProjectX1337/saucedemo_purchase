import pytest
from selenium import webdriver


def pytest_addoption(parser):
    """Хук pytest_addoption для регистрации параметров браузера и URL."""
    parser.addoption(
        "--browser",
        action="store",
        default="chrome",
        help="Браузер для запуска: chrome, firefox или edge",
    )
    parser.addoption(
        "--url",
        action="store",
        default="https://www.saucedemo.com/",
        help="Адрес тестируемого сайта",
    )


@pytest.fixture(scope="session")
def base_url(request):
    """Фикстура для получения url из аргументов командной строки."""
    return request.config.getoption("--url")


@pytest.fixture
def browser(request):
    """Фикстура для работы с браузером с реализацией мультибраузерности."""
    browser_name = request.config.getoption("--browser").lower()
    driver = None

    if browser_name == "chrome":
        driver = webdriver.Chrome()
    elif browser_name == "firefox":
        driver = webdriver.Firefox()
    elif browser_name == "edge":
        driver = webdriver.Edge()
    else:
        raise pytest.UsageError(
            f"Неподдерживаемый браузер '{browser_name}'. Поддерживаются: chrome, firefox, edge."
        )

    driver.maximize_window()
    driver.implicitly_wait(10)

    # Передача управления тесту
    yield driver

    # Закрытие браузера по окончании теста
    driver.quit()