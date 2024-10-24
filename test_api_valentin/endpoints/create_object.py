import requests
import allure

from test_api_valentin.endpoints.endpoints import Endpoints


class CreateObject(Endpoints):

    object_id = None

    @allure.step("Create object")
    def create_object(self, payload, headers=None):
        headers = headers if headers else self.headers
        self.response = requests.post(
            url=self.URL,
            headers=headers,
            json=payload,
        )
        # print(f"ID объекта: {self.response.json()['id']}")
        return self.response
