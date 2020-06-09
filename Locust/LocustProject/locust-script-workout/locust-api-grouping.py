from locust import task, HttpUser, SequentialTaskSet


class Behaviour(SequentialTaskSet):

    @task
    def create_project(self):
        id_list = [1, 2, 3, 4, 5, 6, 7, 8, 9]
        for key in id_list:
            res = self.client.get("/posts/"+str(key), name="get posts api")


class Tasks(HttpUser):
    tasks = [Behaviour]
    host = "https://jsonplaceholder.typicode.com"
    min_wait = 1000
    max_wait = 10000
