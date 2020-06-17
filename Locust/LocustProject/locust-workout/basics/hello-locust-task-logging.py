from locust import User, constant
import logging

def task1(l):
    print("Task 1")


def task2(m):
    print("Task 2")


class Tasks(User):
    tasks = [task1, task2]
    # tasks = {task1: 1, task2: 2}
    wait_time = constant(1)

# Reference: https://docs.locust.io/en/stable/writing-a-locustfile.html
# Command: locust -f hello-locust-task.py
