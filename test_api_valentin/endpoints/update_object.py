import requests

from test_api_valentin.endpoints.endpoints import Endpoints


class UpdateObject(Endpoints):

    def put_change_object(self, payload, object_id, headers=None):
        headers = headers if headers else self.headers
        self.response = requests.put(
            url=f'{self.URL}/{object_id}',
            headers=headers,
            json=payload
        )
        return self.response

    def patch_change_part_of_object(self, payload, object_id, headers=None):
        headers = headers if headers else self.headers
        self.response = requests.patch(
            url=f'{self.URL}/{object_id}',
            headers=headers,
            json=payload
        )
        return self.response
