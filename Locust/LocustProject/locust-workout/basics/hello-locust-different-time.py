from locust import User, between, constant, constant_pacing
import random


def task1(self):
    print("Task 1")


class Tasks(User):
    tasks = [task1]
    # wait_time = constant(1)
    # wait_time = between(1, 3)
    # wait_time = constant_pacing(3)

# Reference: https://docs.locust.io/en/stable/writing-a-locustfile.html
# Command: locust -f hello-locust-task.py
