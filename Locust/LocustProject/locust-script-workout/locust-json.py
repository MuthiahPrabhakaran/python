from locust import task, HttpUser, SequentialTaskSet
import uuid


class Behaviour(SequentialTaskSet):

    @task
    def create_project(self):
        self.token = "123df"
        self.randomid = str(uuid.uuid4())
        resp = self.client.post("/post", json={"name": "project1"},
                                headers={
                                    "Content-Type": "application/json",
                                    "Authorization": "Bearer %s" % self.token,
                                    "X-Requested-Id": self.randomid
                                })

        json_response = resp.json()
        print(json_response)
        print(json_response['headers']['x-requested-id'])


class Tasks(HttpUser):
    tasks = [Behaviour]
    host = "https://postman-echo.com"
    min_wait = 1000
    max_wait = 10000
