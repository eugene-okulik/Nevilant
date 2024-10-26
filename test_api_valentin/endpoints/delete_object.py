import requests

from test_api_valentin.endpoints.endpoints import Endpoints


class DeleteObject(Endpoints):

    def delete_object(self, object_id):
        self.response = requests.delete(
            url=f"{self.URL}/{object_id}",
            headers=self.headers,
        )
        return self.response
