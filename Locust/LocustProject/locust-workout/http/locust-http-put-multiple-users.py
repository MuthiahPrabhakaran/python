from locust import task, HttpUser, TaskSet

users = [(1, "title1"), (2, "title2"), (3, "title3")]


class Behaviour(TaskSet):
    title: str
    key: int

    def on_start(self):
        self.key, self.title = 0, "dummy"
        if len(users) > 0:
            self.key, self.title = users.pop()

    @task
    def hit_post_api(self):
        response = self.client.put("/posts/1", {"id": 1, "title": self.title, "body": "bar", "userId": self.key})
        print(response.text)


class Tasks(HttpUser):
    tasks = [Behaviour]
    host = "https://jsonplaceholder.typicode.com"
    min_wait = 2000
    max_wait = 10000
