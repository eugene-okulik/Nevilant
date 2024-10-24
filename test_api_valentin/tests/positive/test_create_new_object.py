import allure
import pytest

DATA = [
    (
        {
            "name": "Holidays",
            "data": {
                "January": ["New Year Holidays", "Christmas Day"],
                "February": ["Defender of the Fatherland Day"]
            }
        },
        "Blocker"
    ),
    (
        {
            "name": "Выходные",
            "data": {
                "January": ["New Year Holidays", "Christmas Day"],
                "February": ["Defender of the Fatherland Day"]
            }
        },
        "Normal"
    ),
    (
        {
            "name": "Test_ТЕСТ",
            "data": {
                "January": ["New Year Holidays", "Christmas Day"],
                "February": ["Defender of the Fatherland Day"]
            }
        },
        "Normal"
    )
]


@allure.title("Create new object")
@allure.feature("Methods with BODY")
@allure.story("Positive tests")
@pytest.mark.parametrize('data, severity', DATA)
def test_create_post(wrapper_create_object, data, severity):
    allure.dynamic.severity(severity)
    wrapper_create_object.create_object(payload=data)
    wrapper_create_object.check_status_code_is_200()
    wrapper_create_object.check_name(data['name'])
