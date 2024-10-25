import allure


class Endpoints:
    URL = 'http://167.172.172.115:52353/object'
    response = None
    json = None
    headers = {'Content-Type': 'application/json'}

    @allure.step("Check that status code is 200")
    def check_status_code_is_200(self):
        assert self.response.status_code == 200, "Status code is not 200"

    @allure.step("Check object's name")
    def check_name(self, name):
        assert self.response.json()['name'] == name, "Object name is not equal to name"

    @allure.step("Check that status code isn't 200")
    def check_status_code_is_not_200(self):
        assert self.response.status_code != 200, "Status code is 200"

    @allure.step("Check the number of properties")
    def check_properties(self, properties):
        assert len(self.response.json()['data']) == len(properties), "Object properties is not equal to properties"

    @allure.step("Check that object not found")
    def check_object_not_found(self):
        assert self.response.status_code == 404, "Status code is not 404"

    @allure.step("Check that request is wrong")
    def check_bad_request(self):
        assert self.response.status_code == 400, "Status code is not 400"
