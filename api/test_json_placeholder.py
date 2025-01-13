from pytest_check import check
import requests

# Базовый URL для JSONPlaceholder
BASE_URL = "https://jsonplaceholder.typicode.com"

def test_get_posts():
    # Выполняем GET-запрос к /posts
    response = requests.get(f"{BASE_URL}/posts")

    # Проверяем статус код
    with check:
        assert response.status_code == 200, f"Expected status code 200, but got {response.status_code}"

    # Проверяем, что ответ содержит данные
    posts = response.json()
    with check:
        assert len(posts) > 0, "No posts found"


def test_get_post_by_id():
    # Выполняем GET-запрос к /posts/1
    response = requests.get(f"{BASE_URL}/posts/1")

    # Проверяем статус код
    with check:
        assert response.status_code == 200, f"Expected status code 200, but got {response.status_code}"

    # Проверяем, что пост с ID 1 существует
    post = response.json()
    with check:
        assert post["id"] == 1, f"Expected post with ID 1, but got {post['id']}"


def test_create_post():
    # Данные для создания нового поста
    new_post = {
        "title": "foo",
        "body": "bar",
        "userId": 1
    }

    # Выполняем POST-запрос к /posts
    response = requests.post(f"{BASE_URL}/posts", json=new_post)

    # Проверяем статус код
    with check:
        assert response.status_code == 201, f"Expected status code 201, but got {response.status_code}"

    # Проверяем, что пост создан
    created_post = response.json()
    with check:
        assert created_post["title"] == new_post["title"], f"Expected title '{new_post['title']}', but got '{created_post['title']}'"