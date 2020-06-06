from locust import User, constant, TaskSet


def task1(l):
    print("task1")


def task2(m):
    print("task2")


class Set(TaskSet):
    tasks = [task1, task2]


class Tasks(User):
    tasks = [Set]
    wait_time = constant(1)
