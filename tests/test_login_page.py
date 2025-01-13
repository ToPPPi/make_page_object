import pytest
from ..conftest import setup
from ..pages.home_page import LoginPage

@pytest.mark.usefixtures("setup")
class TestLogin:

    #Userdata
    username = "admin"
    password_correct = "admin123"
    password_incorrect = "adminpassword"

    @pytest.fixture(autouse=True)
    def classSetup(self, setup):
        self.lp = LoginPage(self.driver)

    def test_validLogin(self):
        assert self.lp.verifyTitle() == "OrangeHRM"
        assert self.lp.verifyLoginSuccsessful(self.username, self.password_correct) == "Dashboard"

    @pytest.mark.parametrize("username, password", [
        ("admin", "admin"),
        ("admin123", "admin123"),
        ("admin1", "admin1")])
    def test_invalidLogin(self, username, password):
        assert self.lp.verifyLoginIncorrect(username, password) == "Invalid credentials"







