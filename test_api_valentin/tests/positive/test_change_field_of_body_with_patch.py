import allure
import pytest

DATA = [
    (
        {
            "name": "patch"
        },
        "Blocker"
    ),
    (
        {
            "data": {}
        },
        "Blocker"
    )
]


@allure.title("Update object with PATCH method")
@allure.feature("Methods with BODY")
@allure.story("Positive tests")
@pytest.mark.parametrize('data, severity', DATA)
def test_change_field_of_body_with_patch(wrapper_change_object, object_id, data, severity):
    allure.dynamic.severity(severity)
    wrapper_change_object.patch_change_part_of_object(payload=data, object_id=object_id)
    wrapper_change_object.check_status_code_is_200()
