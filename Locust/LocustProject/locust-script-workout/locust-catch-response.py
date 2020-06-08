from locust import task, HttpUser, SequentialTaskSet


class Behaviour(SequentialTaskSet):

    @task
    def launch_url(self):
        self.client.get("/InsuranceWebExtJS/")

    @task
    def login_url(self):
        with self.client.post("/InsuranceWebExtJS/index.jsf"
                , data={"login-form": "login-form", "login-form:email": "qamile2@gmail.com"
                    , "login-form:password": "abc123", "login-form:login.x": "57"
                    , "login-form:login.y": "9", "javax.faces.ViewState": "j_id1:j_id2"},
                              catch_response=True) as response:
            if "Logged in" not in response.text:
                response.failure("User not logged in")
            else:
                response.success()


class Tasks(HttpUser):
    tasks = [Behaviour]
    host = "http://demo.borland.com"
    min_wait = 2000
    max_wait = 10000
