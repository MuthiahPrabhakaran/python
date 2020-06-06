from locust import TaskSet, task, HttpUser


class UserBehaviour(TaskSet):
    @task
    def launch_url(self):
        self.client.get("")


class Tasks(HttpUser):
    tasks = [UserBehaviour]
    host = "http://dummy.restapiexample.com/api/v1/employees"
    min_wait = 2000
    max_wait = 5000
