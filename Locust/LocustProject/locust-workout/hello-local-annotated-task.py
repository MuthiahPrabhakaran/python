from locust import User, constant, task


class Tasks(User):
    @task
    def task1(self):
        print("Task1")

    tasks = [task1]
    min_wait = 2000
    max_wait = 8000
