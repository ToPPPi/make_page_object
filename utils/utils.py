import json
import os

def read_json(file_path):
    # Получаем абсолютный путь к файлу
    absolute_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), file_path)

    # Проверяем, существует ли файл
    if not os.path.exists(absolute_path):
        raise FileNotFoundError(f"Файл не найден: {absolute_path}")

    # Проверяем, что файл не пуст
    if os.path.getsize(absolute_path) == 0:
        raise ValueError(f"Файл пуст: {absolute_path}")

    # Читаем JSON
    with open(absolute_path, "r", encoding="utf-8-sig") as file:
        try:
            data = json.load(file)
        except json.JSONDecodeError as e:
            raise ValueError(f"Некорректный JSON в файле {absolute_path}: {e}")

        return data
