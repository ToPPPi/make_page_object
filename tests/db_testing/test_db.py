import pytest
from ...conftest import db_connection

@pytest.mark.usefixtures("db_connection")
class TestDatabase:
    def test_user_by_id(self):
        with self.connection.cursor() as cursor:
            cursor.execute("SELECT * FROM users WHERE id = 1")
            result = cursor.fetchone()

            assert result is not None, "Пользователь с ID 1 не найден"
            assert result["name"] == "John Doe", f"Ожидалось имя 'John Doe', но получено '{result['name']}'"
            assert result["email"] == "john.doe@example.com", f"Ожидался email 'john.doe@example.com', но получен '{result['email']}'"

    def test_all_users(self):
        with self.connection.cursor() as cursor:
            cursor.execute("SELECT * FROM users")
            results = cursor.fetchall()

            assert len(results) > 0, "В таблице users нет данных"