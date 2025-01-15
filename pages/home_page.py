from selenium.webdriver.common.by import By
from ..base.base_page import BasePage

class LoginPage(BasePage):

    def __init__(self, driver):
        super().__init__(driver)

    #Locators
    _username_field = (By.XPATH, "//*[@name='username']")
    _password_field = (By.XPATH, "//*[@name='password']")
    _login_button = (By.XPATH, "//button[text()=' Login ']")
    _dashboard = (By.XPATH, "//h6[text()='Dashboard']")
    _invalid_credentials = (By.XPATH, "//p[text()='Invalid credentials']")


    # Find Elements (Не использую этот метод, потому как передал нахождения элементов в Locators)
    # def get_Loc_Username(self):
    #     return self.driver.find_element(By.XPATH, self._username_field)
    #
    # def get_Loc_Password(self):
    #     return self.driver.find_element(By.XPATH, self._password_field)
    #
    # def get_Loc_LoginButton(self):
    #     return self.driver.find_element(By.XPATH, self._login_button)
    #
    # def get_Loc_Dashboard(self):
    #     return self.driver.find_element(By.XPATH, self._dashboard)
    #
    # def get_Loc_InvalidCredentials(self):
    #     return self.driver.find_element(By.XPATH, self._invalid_credentials)


    # Assertions
    def verifyLoginSuccsessful(self, username, password_correct):
        self.enter_text(self._username_field, username)
        self.enter_text(self._password_field, password_correct)
        self.click_element(self._login_button)
        return self.get_element_text(self._dashboard)

    def verifyLoginIncorrect(self, username, password_incorrect):
        self.enter_text(self._username_field, username)
        self.enter_text(self._password_field, password_incorrect)
        self.click_element(self._login_button)
        return self.get_element_text(self._invalid_credentials)

    def verifyTitle(self):
        return self.driver.title








