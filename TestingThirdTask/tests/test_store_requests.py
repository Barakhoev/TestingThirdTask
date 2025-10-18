import sys
import os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

import pytest
from base_request import BaseRequest

class StoreRequests(BaseRequest):
    def __init__(self):
        super().__init__('https://petstore.swagger.io/v2')

    def create_order(self, order_data):
        return self.post('/store/order', json=order_data)

    def get_order(self, order_id):
        return self.get(f'/store/order/{order_id}')

    def delete_order(self, order_id):
        return self.delete(f'/store/order/{order_id}')

    def get_inventory(self):
        return self.get('/store/inventory')


@pytest.fixture(scope="module")
def store_api():
    return StoreRequests()


@pytest.fixture(scope="module")
def test_order_data():
    return {
        "id": 1010,
        "petId": 5,
        "quantity": 1,
        "shipDate": "2025-10-17T00:00:00.000Z",
        "status": "placed",
        "complete": True
    }


def test_create_order(store_api, test_order_data):
    """Создание заказа"""
    response = store_api.create_order(test_order_data)
    assert response.status_code == 200
    assert response.json()["id"] == test_order_data["id"]


def test_get_order(store_api, test_order_data):
    """Получение заказа по ID"""
    response = store_api.get_order(test_order_data["id"])
    assert response.status_code in [200, 404]
    if response.status_code == 200:
        data = response.json()
        assert data["id"] == test_order_data["id"]



def test_get_inventory(store_api):
    """Получение инвентаря магазина"""
    response = store_api.get_inventory()
    assert response.status_code == 200
    assert isinstance(response.json(), dict)


def test_delete_order(store_api, test_order_data):
    """Удаление заказа"""
    response = store_api.delete_order(test_order_data["id"])
    assert response.status_code in [200, 404]

