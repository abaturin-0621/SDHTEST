import pytest
import requests
import json
from pytest_cases import  parametrize_with_cases, case, get_case_id, parametrize ,fixture
from pytest_schema import  schema, And, Enum, Optional, Or, Regex, SchemaError
import allure
from utils.attachment import Attach
from utils.error_description import ERR_INVALID_RESPONSE,ERR_INVALID_SCHEMA
from utils.response_description import *
from utils.type_description import OptionalFields, VALID_NONE,VALID_SLASH,VALID_QUOTE,VALID_BOOLEAN_FALSE,VALID_BOOLEAN_TRUE,VALID_NUMBER_INT,VALID_NUMBER_FLOAT,VALID_STRING,VALID_OPTIONAL


URL="http://1.1.0.169:8080/api"
PATH="delivery"
METHOD="DELETE"

##############################################################
@fixture
def EXISTS_DELIVERY_ID(get_exsist_delivery_id):
    """Cуществующий Id DELIVERY"""
    return get_exsist_delivery_id
@fixture    
def EXISTS_ROUTE_ID(get_exsist_route_id):
    """Cуществующий Id ROUTE"""
    return get_exsist_route_id
@fixture 
def EXISTS_SHEDULE_ID(get_exsist_schedule_id):
    """Cуществующий Id SHEDULE"""
    return get_exsist_schedule_id
@fixture 
def EXISTS_SHIPMENT_ID(get_exsist_shipment_id):
    """Cуществующий Id SHIPMENT"""
    return get_exsist_shipment_id     
@fixture 
def EXISTS_TRANSPORT_ID(get_exsist_transport_id):
    """Cуществующий Id TRANSPORT"""
    return get_exsist_transport_id 
##############################################################
@fixture
def NO_EXISTS_DELIVERY_ID(EXISTS_DELIVERY_ID):
    """Не существующий Id DELIVERY"""
    return EXISTS_DELIVERY_ID+1
@fixture    
def NO_EXISTS_ROUTE_ID(EXISTS_ROUTE_ID):
    """Не существующий Id ROUT"""
    return EXISTS_ROUTE_ID+1
@fixture 
def NO_EXISTS_SHEDULE_ID(EXISTS_SHEDULE_ID):
    """Не существующий Id SHEDULE"""
    return EXISTS_SHEDULE_ID+1
@fixture 
def NO_EXISTS_SHIPMENT_ID(EXISTS_SHIPMENT_ID):
    """Не существующий Id SHIPMENT"""
    return EXISTS_SHIPMENT_ID+1     
@fixture 
def NO_EXISTS_TRANSPORT_ID(EXISTS_TRANSPORT_ID):
    """Не существующий Id TRANSPORT"""
    return EXISTS_TRANSPORT_ID+1 

#############################################################
# def create_route_id():  ### не работает
#     """Cоздание  route_id
#      TODO нужна проверка, если список пустой и создание нового
#     """
#     headers={'Content-Type': 'application/json'}
#     body={
#         "origin_attr": {
#             "ip": "test_origin_ip",
#             "port": 2147483647,
#             "username": "test_origin_username",
#             "password": "test_origin_password"
            
#         },
#         "destination_attr": {
#             "ip": "test_dest_ip",
#             "port": 2147483647,
#             "username": "test_destination_username",
#             "password": "test_destination_password"
            
#         },
#         "name": "string",
#         "origin": get_exsist_transport_id(),
#         "destination": get_exsist_transport_id()
#     }
#     url=f"{URL}/route/"
#     response = requests.request(method="POST",url=url,headers=headers,json=body)
#     return response.json()["id"]




# def create_schedule_id():  ### не работает
#     """Cоздание  schedule_id
#      TODO нужна проверка, если список пустой и создание нового
#     """
#     headers={'Content-Type': 'application/json'}
#     body={
#     "name": "test_name",
#     "interval": "test_interval"
#     }
#     url=f"{URL}/schedule/"
#     response = requests.request(method="POST",url=url,headers=headers,json=body)
#     return response.json()["id"]




# def create_transport_id():
#     """Cоздание  transport id
#      TODO нужна проверка, если список пустой и создание нового
#     """
#     headers={'Content-Type': 'application/json'}
#     body={
#     "name": "test_name",
#     "protocol": "test_protocol"
#     }
#     url=f"{URL}/transport/"
#     response = requests.request(method="POST",url=url,headers=headers,json=body)
#     return response.json()["id"]



# def create_shipment_id():
#     """Cоздание  shipment id
#      TODO нужна проверка, если список пустой и создание нового
#     """
#     headers={'Content-Type': 'application/json'}
#     body={
#     "name": "test",
#     "format_group": "test"
#     }
#     url=f"{URL}/shipment/"
#     response = requests.request(method="POST",url=url,headers=headers,json=body)
#     return response.json()["id"]






#######################fixtures#########################################
@fixture
@parametrize("content_type",['application/json'])
def valid_headers(content_type):
    """Параметризация headers, комбинация корректных параметров """
    headers={}
    if not isinstance(content_type,OptionalFields):
         headers["Content-Type"]=content_type
    return headers
################################################################
@fixture
@parametrize("content_type",[VALID_OPTIONAL])
def no_valid_headers(content_type):
    """Параметризация headers, комбинация некорректных параметров """
    headers={}
    if not isinstance(content_type,OptionalFields):
         headers["Content-Type"]=content_type
    return headers
################################################################
@fixture
@parametrize("id",[EXISTS_DELIVERY_ID])
def valid_endpoint(id):
    """Параметризация /{endpoint}, комбинация корректных параметров """
    path={}
    if not isinstance(id,OptionalFields):
         path["id"]=id
    return path
################################################################
@fixture
@parametrize("id",[NO_EXISTS_DELIVERY_ID])
def no_valid_endpoint(id):
    """Параметризация /{endpoint}, комбинация некорректных параметров """
    path={}
    if not isinstance(id,OptionalFields):
         path["id"]=id
    return path
################################################################
@fixture
@parametrize("name",[VALID_STRING(40)])
@parametrize("description",[VALID_STRING(40),VALID_OPTIONAL])
@parametrize("dag_id",[VALID_STRING(100)])
@parametrize("status",[VALID_STRING(15),VALID_OPTIONAL])
# @parametrize("route",[VALID_OPTIONAL,VALID_NUMBER_INT,None,EXISTS_ROUTE_ID])
# @parametrize("schedule",[VALID_OPTIONAL,VALID_NUMBER_INT,None,EXISTS_SHEDULE_ID])
# @parametrize("shipment",[VALID_OPTIONAL,VALID_NUMBER_INT,None,EXISTS_SHIPMENT_ID])
@parametrize("route",[VALID_OPTIONAL,VALID_NONE,EXISTS_ROUTE_ID])
@parametrize("schedule",[VALID_OPTIONAL,VALID_NONE,EXISTS_SHEDULE_ID])
@parametrize("shipment",[VALID_OPTIONAL,VALID_NONE,EXISTS_SHIPMENT_ID])
def valid_extended_body(name,description, dag_id,status,route,schedule,shipment):
    """Параметризация body, комбинация всех корректных параметров """
    body={}
    if not isinstance(name,OptionalFields):
         body["name"]=name 
    if not isinstance(description,OptionalFields):
         body["description"]=description      
    if not isinstance(dag_id,OptionalFields):
         body["dag_id"]=dag_id   
    if not isinstance(status,OptionalFields):
         body["status"]=status 
    if not isinstance(route,OptionalFields):
         body["route"]=route  
    if not isinstance(schedule,OptionalFields):
         body["schedule"]=schedule       
    if not isinstance(shipment,OptionalFields):
         body["shipment"]=shipment                 
    return body

################################################################
@fixture
@parametrize("name",[VALID_STRING(40)])
@parametrize("dag_id",[VALID_STRING(100)])
def valid_optional_body(name, dag_id):
    """Параметризация body, комбинация только обязательных корректных параметров """
    body={}
    if not isinstance(name,OptionalFields):
         body["name"]=name 
    if not isinstance(dag_id,OptionalFields):
         body["dag_id"]=dag_id   
    return body
################################################################

@fixture
@parametrize("name",[VALID_OPTIONAL,VALID_STRING(40+1),VALID_NUMBER_INT,VALID_QUOTE,VALID_SLASH,VALID_NONE])
@parametrize("description",[VALID_NUMBER_INT])
@parametrize("dag_id",[VALID_OPTIONAL,VALID_STRING(100+1)])
@parametrize("status",[VALID_STRING(15+1)])
# @parametrize("route",[VALID_OPTIONAL,VALID_NUMBER_INT,None,EXISTS_ROUTE_ID])
# @parametrize("schedule",[VALID_OPTIONAL,VALID_NUMBER_INT,None,EXISTS_SHEDULE_ID])
# @parametrize("shipment",[VALID_OPTIONAL,VALID_NUMBER_INT,None,EXISTS_SHIPMENT_ID])
@parametrize("route",[NO_EXISTS_ROUTE_ID,VALID_STRING(40+1)])
@parametrize("schedule",[NO_EXISTS_SHEDULE_ID,VALID_STRING(40+1)])
@parametrize("shipment",[NO_EXISTS_SHIPMENT_ID,VALID_STRING(40+1)])
def no_valid_body(name,description, dag_id,status,route,schedule,shipment):
    """Параметризация body, комбинация некорректных параметров """
    body={}
    if not isinstance(name,OptionalFields):
         body["name"]=name 
    if not isinstance(description,OptionalFields):
         body["description"]=description      
    if not isinstance(dag_id,OptionalFields):
         body["dag_id"]=dag_id   
    if not isinstance(status,OptionalFields):
         body["status"]=status 
    if not isinstance(route,OptionalFields):
         body["route"]=route  
    if not isinstance(schedule,OptionalFields):
         body["schedule"]=schedule       
    if not isinstance(shipment,OptionalFields):
         body["shipment"]=shipment                 
    return body

################################################################
@fixture
def valid_response_schema():
    """Параметризация response_schema ,соcтавляется на основании свагера"""
    response_schema={
        "id": int,
        "name": str,
        "description": Or(None, str),
        "dag_id": str,
        "status": str,
        "route": Or(None, int),
        "schedule": Or(None, int),
        "shipment": Or(None, int)
    }  
    return response_schema

################################TEST####################################################
@allure.feature('delivery')
@allure.feature('delivery delete by id')
@allure.suite("check body")
@allure.story('positive')    
@allure.story('response 204') 
@allure.testcase("https://cdp.colvir.ru/wiki/display/SDH/A000002", 'A000002')
@allure.description("""
     Запрос на удаление delivery с корректными параметрами 
     Ожидаемый результат: response.status_code=204 """)
@parametrize("headers",[valid_headers]) 
@parametrize("endpoints",[valid_endpoint]) 
@parametrize("status_code",[RESPONSE_NO_CONTENT]) 
@allure.title("Запрос на удаление delivery с корректными параметрами")
def test_all_valid_parameters(headers,endpoints,status_code):
    id=endpoints["id"]
    url=f"{URL}/{PATH}/{id}/"

    response = requests.request(method=METHOD,url=url, headers=headers )

    Attach(url=url,headers=headers).attach() 
    assert response.status_code==status_code,ERR_INVALID_RESPONSE

####################################################################################

@allure.feature('delivery')
@allure.feature('delivery delete by id')
@allure.suite("check headers")
@allure.story('negative')    
@allure.story('response 415') 
@allure.testcase("https://cdp.colvir.ru/wiki/display/SDH/A000003", 'A000003')
@allure.description(""" 
    Запрос на удаление delivery с некорректным headers
    Ожидаемый результат: response.status_code=415
                    """)
@parametrize("headers",[no_valid_headers]) 
@parametrize("endpoints",[valid_endpoint]) 
@parametrize("status_code",[RESPONSE_UNSUPPORTED]) 
@allure.title("Запрос на удаление delivery с некорректным headers")
def test_invalid_header(headers,endpoints,status_code):
    id=endpoints["id"]
    url=f"{URL}/{PATH}/{id}/"
    
    response = requests.request(method=METHOD,url=url, headers=headers)

    Attach(url=url,headers=headers,response=response.json()).attach() 

    assert response.status_code==status_code,ERR_INVALID_RESPONSE

####################################################################################
 
@allure.feature('delivery')
@allure.feature('delivery delete by id')
@allure.suite("check endpoint")
@allure.story('negative')    
@allure.story('response 404') 
@allure.testcase("https://cdp.colvir.ru/wiki/display/SDH/A000002", 'A000002')
@allure.description("""
    Запрос на удаление delivery с некорректным endpoint 
    Ожидаемый результат: response.status_code=404
#  """)
@parametrize("headers",[valid_headers]) 
@parametrize("endpoints",[no_valid_endpoint]) 
@parametrize("status_code",[RESPONSE_NOT_FOUND]) 
@allure.title("Запрос на удаление delivery с  некорректным endpoint ")
def test_invalid_endpoints(headers,endpoints,status_code):
    id=endpoints["id"]
    url=f"{URL}/{PATH}/{id}/"
       
    response = requests.request(method=METHOD,url=url, headers=headers )

    Attach(url=url,headers=headers,response=response.json()).attach() 

    assert response.status_code==status_code,ERR_INVALID_RESPONSE
####################################################################################



