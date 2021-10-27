import pytest
from pytest_cases import fixture
import requests

@pytest.fixture(scope="module")
def URL():
    return "http://1.1.0.169:8080/api"

@pytest.fixture(scope="module")
def get_exsist_delivery_id(URL):
    """Получение существующего  delivery id 
     TODO нужна проверка, если список пустой и создание нового
    """
    url=f"{URL}/delivery/"
    response = requests.request(method="GET",url=url)
    return max([x["id"] for x in  response.json()])

@pytest.fixture(scope="module")
def get_exsist_route_id(URL):
    """Получение существующего  route id
     TODO нужна проверка, если список пустой и создание нового
    """
    url=f"{URL}/route/"
    response = requests.request(method="GET",url=url)
    return max([x["id"] for x in  response.json()])

@pytest.fixture(scope="module")
def get_exsist_schedule_id(URL):
    """Получение существующего  schedule id
     TODO нужна проверка ,если список пустой и создание нового
    """
    url=f"{URL}/schedule/"
    response = requests.request(method="GET",url=url)
    return max([x["id"] for x in  response.json()])

@pytest.fixture(scope="module")
def get_exsist_shipment_id(URL):
    """Получение существующего  shipment id
     TODO нужна проверка, если список пустой и создание нового
    """
    url=f"{URL}/shipment/"
    response = requests.request(method="GET",url=url)
    return max([x["id"] for x in  response.json()])

@pytest.fixture(scope="module")
def get_exsist_transport_id(URL):
    """Получение существующего  transport id
     TODO нужна проверка, если список пустой и создание нового
    """
    url=f"{URL}/transport/"
    response = requests.request(method="GET",url=url)
    return max([x["id"] for x in  response.json()])