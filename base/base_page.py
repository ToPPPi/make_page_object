from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains


class BasePage:
    def __init__(self, driver):
        self.driver = driver
        self.actions = ActionChains(driver)
        self.wait = WebDriverWait(self.driver, 10)

    # Actions
    def wait_for_element(self, locator):
        """Ожидает появления элемента на странице."""
        return self.wait.until(EC.visibility_of_element_located(locator))

    def click_element(self, locator):
        """Кликает по элементу."""
        self.wait_for_element(locator).click()

    def enter_text(self, locator, text):
        """Вводит текст в поле."""
        self.wait_for_element(locator).send_keys(text)

    def get_element_text(self, locator):
        """Возвращает текст элемента."""
        return self.wait_for_element(locator).text