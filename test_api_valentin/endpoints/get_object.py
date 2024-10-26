import allure
import requests

from test_api_valentin.endpoints.endpoints import Endpoints


class GetObject(Endpoints):

    @allure.step("Get object by ID")
    def get_object(self, object_id, headers=None):
        headers = headers if headers else self.headers
        self.response = requests.get(
            url=f'{self.URL}/{object_id}',
            headers=headers,
        )
        self.json = self.response.json()
        print(f"Get object by ID: {object_id}. Response: {self.json}")
        return self.response
