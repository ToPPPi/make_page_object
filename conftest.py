import pytest
import os
import shutil
import pymysql
from selenium import webdriver
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.firefox.options import Options as FirefoxOptions
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager


@pytest.fixture(params=["chrome", "firefox"])  # Параметризация для выбора браузера
def setup(request):
    # Получаем значение аргумента --browser, если он передан
    browser_name = request.config.getoption("--browser", default=request.param)

    if os.getenv("CI") == "true":  # Проверяем, запущены ли тесты в CI/CD
        # Используем Selenium Grid
        if browser_name == "chrome":
            options = ChromeOptions()
        elif browser_name == "firefox":
            options = FirefoxOptions()

        # Настройки для headless-режима
        options.add_argument("--headless")
        options.add_argument("--no-sandbox")
        options.add_argument("--disable-dev-shm-usage")

        driver = webdriver.Remote(command_executor="http://localhost:4444/wd/hub", options=options)

    else:
        # Используем локальные драйверы
        if request.param == "chrome":
            chrome_options = ChromeOptions()
            chrome_options.add_argument("--headless")  # Включаем headless mode
            driver = webdriver.Chrome(service=webdriver.chrome.service.Service(ChromeDriverManager().install()), options=chrome_options)
        elif request.param == "firefox":
            firefox_options = FirefoxOptions()
            firefox_options.add_argument("--headless")  # Включаем headless mode
            driver = webdriver.Firefox(service=webdriver.firefox.service.Service(GeckoDriverManager().install()), options=firefox_options)

    driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
    driver.implicitly_wait(5)

    request.cls.driver = driver

    yield
    driver.quit()

def pytest_addoption(parser):
    parser.addoption(
        "--browser", action="store", default="chrome", help="Браузер для тестов: chrome или firefox"
    )

@pytest.fixture(scope="session", autouse=True)
def clean_allure_results():
    # Очистка папки allure-results перед запуском тестов
    if os.path.exists("allure-results"):
        try:
            shutil.rmtree("allure-results")
        except FileNotFoundError:
            # Если папка уже удалена, игнорируем ошибку
            pass
    os.makedirs("allure-results", exist_ok=True)


# Фикстура для подключения к базе данных
@pytest.fixture
def db_connection(request):
    # Подключение к базе данных
    try:
        connection = pymysql.connect(
            #host="db", #Работает если запускать через GitHub
            host="127.0.0.1", #Работает локально
            user="root",
            password="admin",
            database="testdb",
            cursorclass=pymysql.cursors.DictCursor
        )

        request.cls.connection = connection

        yield connection
        connection.close()
    except pymysql.Error:
        pytest.skip("База данных недоступна")
