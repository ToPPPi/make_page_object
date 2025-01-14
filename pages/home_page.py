from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait

class LoginPage:

    def __init__(self, driver):
        self.driver = driver
        self.actions = ActionChains(driver)
        self.wait = WebDriverWait(self.driver, 10)

    #Locators
    _username_field = "//*[@name='username']"
    _password_field = "//*[@name='password']"
    _login_button = "//button[text()=' Login ']"
    _dashboard = "//h6[text()='Dashboard']"
    _invalid_credentials = "//p[text()='Invalid credentials']"


    # Find Elements
    def get_Loc_Username(self):
        return self.driver.find_element(By.XPATH, self._username_field)

    def get_Loc_Password(self):
        return self.driver.find_element(By.XPATH, self._password_field)

    def get_Loc_LoginButton(self):
        return self.driver.find_element(By.XPATH, self._login_button)

    def get_Loc_Dashboard(self):
        return self.driver.find_element(By.XPATH, self._dashboard)

    def get_Loc_InvalidCredentials(self):
        return self.driver.find_element(By.XPATH, self._invalid_credentials)


    # Actions
    def enterUsername(self, username):
        self.get_Loc_Username().send_keys(username)

    def enterPassword(self, password):
        self.get_Loc_Password().send_keys(password)

    def clickLoginButton(self):
        self.get_Loc_LoginButton().click()

    def textDashboard(self):
        return self.get_Loc_Dashboard().text

    def textInvalidCredentials(self):
        return self.get_Loc_InvalidCredentials().text


    # Assertions
    def verifyLoginSuccsessful(self, username, password_correct):
        self.enterUsername(username)
        self.enterPassword(password_correct)
        self.clickLoginButton()
        dashboard_text = self.textDashboard()
        return dashboard_text

    def verifyLoginIncorrect(self, username, password_incorrect):
        self.enterUsername(username)
        self.enterPassword(password_incorrect)
        self.clickLoginButton()
        invalidCredentials_text = self.textInvalidCredentials()
        return invalidCredentials_text

    def verifyTitle(self):
        title = self.driver.title
        return title








