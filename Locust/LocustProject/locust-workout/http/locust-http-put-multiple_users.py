from locust import task, HttpUser, TaskSet
import logging

users = [(1, "title1"), (2, "title2"), (3, "title3")]


class Behaviour(TaskSet):
    @task
    def hit_post_api(self):
        response = self.client.put("", {"id": 1, "title": "foo", "body": "bar", "userId": 1})
        # self.client.put("", data={"id": 1, "title": "foo", "body": "bar", "userId": 1})

        # print out the response elements
        # print(response.status_code)
        # print(response.headers)
        # print(response.request.headers)

        # This is what we might need
        # print(response.text)
        logging.info(response.text)


class Tasks(HttpUser):
    tasks = [Behaviour]
    host = "https://jsonplaceholder.typicode.com/posts/1"
    min_wait = 2000
    max_wait = 10000
