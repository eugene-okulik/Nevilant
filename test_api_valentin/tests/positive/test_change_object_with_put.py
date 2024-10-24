import allure
import pytest

DATA = [
    (
        {
            "name": "test",
            "data":
                {
                    "test": "idk"
                }
        },
        "Blocker"
    ),
    (
        {
            "name": "",
            "data": {}
        },
        "Minor"
    )
]


@allure.title("Update object with PUT method")
@allure.feature("Methods with BODY")
@allure.story("Positive tests")
@pytest.mark.parametrize('data, severity', DATA)
def test_change_object_with_put(wrapper_change_object, object_id, data, severity):
    allure.dynamic.severity(severity)
    wrapper_change_object.put_change_object(payload=data, object_id=object_id)
    wrapper_change_object.check_status_code_is_200()
    wrapper_change_object.check_properties(data['data'])
