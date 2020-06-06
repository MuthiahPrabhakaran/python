from locust import task, HttpUser, TaskSet


class Behaviour(TaskSet):
    @task
    def hit_post_api(self):
        self.client.put("", {"id": 1, "title": "foo", "body": "bar", "userId": 1})
        # self.client.put("", data={"id": 1, "title": "foo", "body": "bar", "userId": 1})


class Tasks(HttpUser):
    tasks = [Behaviour]
    host = "https://jsonplaceholder.typicode.com/posts/1"
    min_wait = 2000
    max_wait = 10000
