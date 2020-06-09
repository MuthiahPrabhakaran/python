from locust import task, HttpUser, TaskSet
from data import user_data


class Behaviour(TaskSet):
    title: str
    key: int

    def on_start(self):
        self.key, self.title = 0, "dummy"
        if len(user_data.user_id_list) > 0:
            self.key, self.title = user_data.user_id_list.pop()

    @task
    def hit_post_api(self):
        response = self.client.put("/posts/1", {"id": 1, "title": self.title, "body": "bar", "userId": self.key})
        print(self.key)


class Tasks(HttpUser):
    tasks = [Behaviour]
    host = "https://jsonplaceholder.typicode.com"
    min_wait = 2000
    max_wait = 10000
