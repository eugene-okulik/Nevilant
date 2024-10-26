import allure


@allure.title("Getting object")
@allure.feature("Methods without BODY")
@allure.story("Positive tests")
@allure.severity("Blocker")
def test_get_object(wrapper_get_object, object_id):
    wrapper_get_object.get_object(object_id)
    wrapper_get_object.check_status_code_is_200()
