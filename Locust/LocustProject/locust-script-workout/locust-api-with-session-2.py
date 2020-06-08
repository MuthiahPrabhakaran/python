from locust import task, HttpUser, SequentialTaskSet


class Behaviour(SequentialTaskSet):

    @task
    def launch_url(self):
        global res
        res = self.client.get("/InsuranceWebExtJS/")
        # print(res.cookies['JSESSIONID'])

        global res2
        with self.client.post("/InsuranceWebExtJS/index.jsf",
                              {"login-form": "login-form", "login-form:email": "john.smith@gmail.com",
                               "login-form:password": "john", "login-form:login.x": "47"
                                  , "login-form:login.y": "5", "javax.faces.ViewState": "j_id1:j_id2"},
                              cookies={"JSESSIONID": res.cookies['JSESSIONID']},
                              catch_response=True) as response:
            if "Logged in" not in response.text:
                response.failure("User not logged in")
            else:
                response.success()
                print("User logged in")
                res2 = response.cookies['UserSessionFilter.sessionId']

    @task
    def auth_quote(self):
        with self.client.get("/InsuranceWebExtJS/quote_auto.jsf",
                             cookies={"JSESSIONID": res.cookies['JSESSIONID'], "UserSessionFilter.sessionId": res2},
                             catch_response=True) as response:
            if "Get Instant Auto Quote" not in response.text:
                response.failure("quote is not there")
            else:
                response.success()
                print("Received quote")


class Tasks(HttpUser):
    tasks = [Behaviour]
    host = "http://demo.borland.com"
    min_wait = 2000
    max_wait = 10000
