import pytest
from pytest_check import check
import allure
from ..conftest import setup
from ..pages.home_page import LoginPage
from ..utils.utils import read_json


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
    @pytest.mark.parametrize("test_data", read_json("../test_data/testing_data.json"))
    def test_invalidLogin(self, test_data):
        with allure.step("Проверка неуспешной авторизации"):
            with check:
                assert self.lp.verifyLoginIncorrect(test_data["username"], test_data["password"]) == test_data["expected"]






