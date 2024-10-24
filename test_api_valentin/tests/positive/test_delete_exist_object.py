import allure


@allure.title("Delete object")
@allure.feature("Methods without BODY")
@allure.story("Positive tests")
@allure.severity("Blocker")
def test_delete_object(wrapper_delete_object, object_id):
    wrapper_delete_object.delete_object(object_id)
    wrapper_delete_object.check_status_code_is_200()
