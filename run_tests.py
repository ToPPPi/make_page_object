import pytest


if __name__ == "__main__":
    # Запуск всех тестов
    pytest.main(["-v", "-n", "4", "tests/", "api/", "--alluredir=allure-results"])