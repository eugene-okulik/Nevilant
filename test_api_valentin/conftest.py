import pytest

from test_api_valentin.endpoints.create_object import CreateObject
from test_api_valentin.endpoints.delete_object import DeleteObject
from test_api_valentin.endpoints.get_object import GetObject
from test_api_valentin.endpoints.update_object import UpdateObject


@pytest.fixture()
def wrapper_create_object():
    return CreateObject()


@pytest.fixture()
def wrapper_get_object():
    return GetObject()


@pytest.fixture()
def wrapper_delete_object():
    return DeleteObject()


@pytest.fixture()
def wrapper_change_object():
    return UpdateObject()


@pytest.fixture()
def object_id(wrapper_create_object):
    payload = {
        "name": "Holidays",
        "data": {
            "January": ["New Year Holidays", "Christmas Day"],
            "February": ["Defender of the Fatherland Day"]
        }
    }
    wrapper_create_object.create_object(payload=payload)
    object_id = wrapper_create_object.response.json()['id']
    yield object_id
