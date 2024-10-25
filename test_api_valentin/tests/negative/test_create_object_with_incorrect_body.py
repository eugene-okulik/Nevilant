import allure
import pytest

DATA = [
    {
        "name": "Holidays",
        "data": "TEST"
    },
    {
        "name": "Vacations",
        "data": 123
    },
    {
        "name": "Celebrations",
    },

]


@allure.title("Create new object")
@allure.feature("Methods with BODY")
@allure.story("Negative tests")
@pytest.mark.parametrize('data', DATA)
def test_create_object_with_incorrect_body(wrapper_create_object, data):
    wrapper_create_object.create_object(payload=data)
    wrapper_create_object.check_bad_request()
