from locust import task, HttpUser, TaskSet
import csv


class Behaviour(TaskSet):
    title: str
    key: int

    def on_start(self):
        self.key, self.title = 0, "dummy"
        if len(user_data) > 0:
            self.key, self.title = user_data.pop()

    @task
    def hit_post_api(self):
        response = self.client.put("/posts/1", {"id": 1, "title": self.title, "body": "bar", "userId": self.key})
        print(self.key)


class Tasks(HttpUser):
    tasks = [Behaviour]
    host = "https://jsonplaceholder.typicode.com"
    min_wait = 2000
    max_wait = 10000

    # Read CSV file
    def on_start(self):
        global user_data
        with open("C:\\Users\\Dallps\\Documents\\SourceTree\\Python\\Locust-CSV\\data\\user_data.csv", 'rt') as file:
            csv_reader = csv.reader(file)
            # for line in csv_reader:
            #      print(line)
            user_data = list(csv_reader)
