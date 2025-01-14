import pytest
from pytest_check import check
import allure
from ..conftest import setup
from ..pages.home_page import LoginPage

@pytest.mark.usefixtures("setup")
@allure.feature("Тесты для авторизации")
class TestLogin:

    #Userdata
    username = "admin"
    password_correct = "admin123"
    password_incorrect = "adminpassword"

    @pytest.fixture(autouse=True)
    def classSetup(self, setup):
        self.lp = LoginPage(self.driver)


    @allure.story("Проверка успешной авторизации")
    @allure.title("Тест успешной авторизации")
    def test_validLogin(self):
        with allure.step("Проверка заголовка страницы"):
            with check:
                assert self.lp.verifyTitle() == "OrangeHRMM"
        with allure.step("Проверка успешной авторизации"):
            with check:
                assert self.lp.verifyLoginSuccsessful(self.username, self.password_correct) == "Dashboard"


    @allure.story("Проверка неуспешной авторизации")
    @allure.title("Тест неуспешной авторизации")
    @pytest.mark.parametrize("username, password", [
        ("admin", "admin"),
        ("admin123", "admin123"),
        ("admin1", "admin1")])
    def test_invalidLogin(self, username, password):
        with allure.step("Проверка неуспешной авторизации"):
            with check:
                assert self.lp.verifyLoginIncorrect(username, password) == "Invalid credentials"






