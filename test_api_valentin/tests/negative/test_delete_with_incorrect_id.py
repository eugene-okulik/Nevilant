import allure
import pytest


NOT_EXIST_ID = [
    99999999, "abc", " "
]


@allure.title("Delete object")
@allure.feature("Methods without BODY")
@allure.story("Negative tests")
@pytest.mark.parametrize("data", NOT_EXIST_ID)
def test_delete_with_incorrect_id(wrapper_delete_object, data):
    wrapper_delete_object.delete_object(data)
    wrapper_delete_object.check_object_not_found()
