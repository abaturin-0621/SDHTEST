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

@allure.feature('schedule')
@allure.feature('schedule patch by id')
@allure.suite("skipped")
@allure.description("Метод  schedule PATCH будет исключен")
@allure.title("Метод  schedule PATCH будет исключен")
@pytest.mark.skip(reason="Метод будет исключен")
def test_template():
     pass