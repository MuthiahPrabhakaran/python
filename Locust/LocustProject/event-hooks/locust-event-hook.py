from locust import User, task
from locust.event import EventHook

custom_event1 = EventHook()
custom_event2 = EventHook()


def handler1(a, b, **kwargs):
    print("sum :", a + b)


def handler2(a, b, **kwargs):
    print("diff :", a - b)


custom_event1.add_listener(handler1)
custom_event2.add_listener(handler2)


class Tasks(User):
    @task
    def task1(self):
        print("Task1")
        flag = False
        if flag:
            custom_event1.fire(a=2, b=1, msg="event1 fired")
        else:
            custom_event2.fire(a=2, b=1, msg="event2 fired")


    tasks = [task1]
    min_wait = 2000
    max_wait = 8000
