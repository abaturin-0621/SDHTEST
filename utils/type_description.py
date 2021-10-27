from random import choice
from string import ascii_uppercase,ascii_lowercase
import datetime

class OptionalFields:
    """ Класс заглушка для обозначения необязательных параметров"""
    pass

def det_valid_date():
    """Дата , пока что одна"""
    return datetime.datetime(2000, 1, 1).strftime("%Y-%m-%d")

def get_valid_none():
    return None
def get_valid_boolean(_bool=True):
    return _bool   
def get_valid_number_int():
    return 1    
def get_valid_number_float():
    return 1.0 
def get_valid_string(size=5):
    return ''.join(choice(ascii_lowercase) for i in range(size))

def get_valid_length_string(size=5):
    return ''.join(choice(ascii_lowercase) for i in range(size))

def get_valid_slash():
    return "\\"
def get_valid_quote():
    return """"""

def get_valid_number(number=0):
    return number

VALID_DATETIME=det_valid_date() ## дата 2000-01-01 01:01:01


VALID_OPTIONAL=OptionalFields()  ### признак необязательных полей

VALID_NONE=get_valid_none()   ### None

VALID_BOOLEAN=get_valid_boolean  
VALID_BOOLEAN_TRUE=VALID_BOOLEAN()  ### True
VALID_BOOLEAN_FALSE=VALID_BOOLEAN(False)  ### False

VALID_NUMBER=get_valid_number  ### заданное число пример использования VALID_NUMBER(-2147483647)
VALID_NUMBER_INT=get_valid_number_int()  ### int number
VALID_NUMBER_FLOAT=get_valid_number_float()  ### float number

VALID_STRING=get_valid_string    ##Произвольная строка заданной длины , пример использования VALID_STRING(5)
VALID_SHORT_STRING=get_valid_length_string
VALID_LONG_STRING=get_valid_length_string

VALID_SLASH=get_valid_slash()  ## Слэш
VALID_QUOTE=get_valid_quote()  ## Кавычки


