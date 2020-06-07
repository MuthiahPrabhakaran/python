from locust import task, HttpUser, SequentialTaskSet


class Behaviour(SequentialTaskSet):

    @task
    def task1(self):
        self.client.put("/posts/1", {"id": 1, "title": "title", "body": "bar", "userId": 1})

    @task
    def get_post(self):
        self.client.get("/posts/1")

    @task
    def get_comment(self):
        self.client.get("/posts/1/comments")

    @task
    def del_post(self):
        self.client.delete("/posts/1")

    # tasks = [task1, get_post, get_comment, del_post]


class Tasks(HttpUser):
    tasks = [Behaviour]
    host = "https://jsonplaceholder.typicode.com"
    min_wait = 2000
    max_wait = 10000

# To run without web
# locust -f locust-http-task-sequence.py --headless -u 5 -r 2
# https://docs.locust.io/en/stable/running-locust-without-web-ui.html
