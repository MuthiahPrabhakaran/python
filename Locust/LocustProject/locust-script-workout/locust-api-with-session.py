from locust import task, HttpUser, SequentialTaskSet


class Behaviour(SequentialTaskSet):

    @task
    def launch_url(self):
        global res
        res = self.client.get("/InsuranceWebExtJS/")
        print(res.cookies['JSESSIONID'])

    @task
    def login_url(self):
        with self.client.post("/InsuranceWebExtJS/index.jsf",
                              {"login-form": "login-form", "login-form:email": "john.smith@gmail.com",
                               "login-form:password": "john", "login-form:login.x": "47"
                                  , "login-form:login.y": "5", "javax.faces.ViewState": "j_id1:j_id2"},
                              cookies={"JSESSIONID": res.cookies['JSESSIONID']},
                              catch_response=True) as response:
            if "Logged in" not in response.text:
                response.failure("User not logged in")
            else:
                print("User logged in")
                print('User session cookie = '+response.cookies['UserSessionFilter.sessionId'])
                response.success()


class Tasks(HttpUser):
    tasks = [Behaviour]
    host = "http://demo.borland.com"
    min_wait = 2000
    max_wait = 10000
