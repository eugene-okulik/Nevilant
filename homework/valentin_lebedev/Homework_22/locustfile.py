from locust import HttpUser, task


class WorkWithObjects(HttpUser):
    headers = {'Content-Type': 'application/json'}
    body = {
        "name": "Hello",
        "data": {
            "message": "Hello Testers",
        }
    }

    object_id = None

    def on_start(self):
        response = self.client.post(
            f'/object',
            headers=self.headers,
            json=self.body
        )
        self.object_id = response.json().get('id')

    def on_stop(self):
        self.client.delete(
            f'/object/{self.object_id}',
            headers=self.headers
        )

    @task(1)
    def get_all_objects(self):
        self.client.get(
            '/object',
            headers=self.headers
        )

    @task(3)
    def get_one_object(self):
        if self.object_id:
            self.client.get(
                f'/object/{self.object_id}',
                headers=self.headers
            )

    @task(2)
    def change_object_with_patch(self):
        body = {
            "name": "patch"
        }
        self.client.patch(
            f'/object/{self.object_id}',
            headers=self.headers,
            json=body
        )
