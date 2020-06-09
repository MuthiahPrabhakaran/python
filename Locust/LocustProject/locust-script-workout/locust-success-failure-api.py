from locust import task, HttpUser, SequentialTaskSet
import locust.stats

locust.stats.CSV_STATS_INTERVAL_SEC = 5  # 2 is default


class Behaviour(SequentialTaskSet):

    @task
    def success_response(self):
        self.client.get("/200")

    @task
    def login_url(self):
        with self.client.get("/400",
                             catch_response=True) as response:
            if "Bad Request" in response.text:
                response.failure("Bad request")
            else:
                response.success()


class Tasks(HttpUser):
    tasks = [Behaviour]
    host = "https://httpstat.us"
    min_wait = 2000
    max_wait = 10000
