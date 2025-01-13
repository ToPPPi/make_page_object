import pytest
from selenium import webdriver
from get_chrome_driver import GetChromeDriver
from selenium.webdriver.chrome.options import Options

@pytest.fixture()
def setup(request):
    chrome_options = Options()
    chrome_options.add_argument("--headless")  # Включаем headless mode
    chrome_options.add_argument("--no-sandbox")  # Отключаем sandbox для CI/CD
    chrome_options.add_argument("--disable-dev-shm-usage")  # Решает проблемы с памятью в CI/CD

    get_driver = GetChromeDriver()
    get_driver.install()
    driver = webdriver.Chrome(options=chrome_options)
    driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
    driver.implicitly_wait(5)

    request.cls.driver = driver

    yield
    driver.quit()
