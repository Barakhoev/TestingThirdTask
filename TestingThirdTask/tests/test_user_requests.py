import sys
import os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

import pytest
from base_request import BaseRequest

class UserRequests(BaseRequest):
    def __init__(self):
        super().__init__('https://petstore.swagger.io/v2')

    def create_user(self, user_data):
        return self.post('/user', json=user_data)

    def get_user(self, username):
        return self.get(f'/user/{username}')

    def update_user(self, username, user_data):
        return self.put(f'/user/{username}', json=user_data)

    def delete_user(self, username):
        return self.delete(f'/user/{username}')


@pytest.fixture(scope="module")
def user_api():
    return UserRequests()


@pytest.fixture(scope="module")
def test_user_data():
    return {
        "id": 9999,
        "username": "pytest_user",
        "firstName": "Test",
        "lastName": "User",
        "email": "test@user.com",
        "password": "12345",
        "phone": "1234567890",
        "userStatus": 1
    }


def test_create_user(user_api, test_user_data):
    """Создание пользователя"""
    response = user_api.create_user(test_user_data)
    assert response.status_code == 200
    assert response.json()["message"] == str(test_user_data["id"])


def test_get_user(user_api, test_user_data):
    """Получение информации о пользователе"""
    response = user_api.get_user(test_user_data["username"])
    assert response.status_code in [200, 404]
    if response.status_code == 200:
        data = response.json()
        assert data["username"] == test_user_data["username"]



def test_update_user(user_api, test_user_data):
    """Обновление данных пользователя"""
    updated_data = test_user_data.copy()
    updated_data["firstName"] = "Updated"
    response = user_api.update_user(test_user_data["username"], updated_data)
    assert response.status_code == 200
    assert response.json()["message"] == str(test_user_data["id"])



def test_delete_user(user_api, test_user_data):
    """Удаление пользователя"""
    response = user_api.delete_user(test_user_data["username"])
    assert response.status_code in [200, 404]

