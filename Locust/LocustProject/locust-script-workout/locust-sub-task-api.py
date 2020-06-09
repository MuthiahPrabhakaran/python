from locust import HttpUser, TaskSet, between, task
import re

header = {
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3",
    "Accept-Encoding": "gzip, deflate, br",
    "Accept-Language": "en-US,en;q=0.9",
    "Connection": "keep-alive",
    "Host": "demo.borland.com",
    "Sec-Fetch-Mode": "navigate",
    "Sec-Fetch-Site": "same-origin",
    "Sec-Fetch-User": "?1",
    "Upgrade-Insecure-Requests": "1",
    "Content-Type": "application/x-www-form-urlencoded",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.120 Safari/537.36"
}


class AgentLookUp(TaskSet):
    print("In AgentLookup")

    @task()
    def choose_service_agentlookup(self):
        with self.client.get("/InsuranceWebExtJS/agent_lookup.jsf",
                             cookies={'JSESSIONID': self.parent.res.cookies['JSESSIONID'],
                                      'UserSessionFilter.sessionId':
                                          self.parent.res2.cookies[
                                              'UserSessionFilter.sessionId']},
                             headers=header,
                             catch_response=True) as self.resA3:

            if "Find an Insurance " not in self.resA3.text:
                self.resA.failure("Got wrong response")
            else:
                self.resA3.success()
                re2 = re.findall("j_id\d+:j_id\d+", self.resA3.text)
                self.viewstateA2 = re2[0]
                print("res3" + self.resA3.text)
                print("viewstate2" + self.viewstateA2)

    @task()
    def agent_search(self):

        with self.client.post("/InsuranceWebExtJS/agent_lookup.jsf", headers=header, data={"show-all": "show-all",
                                                                                           "show-all:search-all.x": "42",
                                                                                           "show-all:search-all.y": "8",
                                                                                           "javax.faces.ViewState": self.viewstateA2},
                              cookies={'JSESSIONID': self.parent.res.cookies['JSESSIONID'],
                                       'UserSessionFilter.sessionId': self.parent.res2.cookies[
                                           'UserSessionFilter.sessionId']},
                              catch_response=True) as self.resA4:

            if "Insurance Agent Search Results" not in self.resA4.text:
                self.resA4.failure("Got wrong response")
                print(self.resA4.text)
            else:
                self.resA4.success()

    @task()
    def stop(self):
        self.interrupt()


class AutoQuote(TaskSet):

    @task()
    def choose_service_autoquote(self):
        with self.client.get("/InsuranceWebExtJS/quote_auto.jsf",
                             cookies={'JSESSIONID': self.parent.res.cookies['JSESSIONID'],
                                      'UserSessionFilter.sessionId':
                                          self.parent.res2.cookies[
                                              'UserSessionFilter.sessionId']},
                             headers=header,
                             catch_response=True) as self.res3:

            if "Get Instant Auto Quote" not in self.res3.text:
                self.res3.failure("Got wrong response")
            else:
                self.res3.success()
                re2 = re.findall("j_id\d+:j_id\d+", self.res3.text)

                self.viewstate2 = re2[0]
                print("viewstate2" + self.viewstate2)

    @task()
    def getinstantquote_1(self):
        with self.client.post("/InsuranceWebExtJS/quote_auto.jsf", headers=header, data={"autoquote": "autoquote",
                                                                                         "autoquote:zipcode": "00000000",
                                                                                         "autoquote:e-mail": "qamile2@gmail.com",
                                                                                         "autoquote:vehicle": "car",
                                                                                         "autoquote:next.x": "38",
                                                                                         "autoquote:next.y": "10",
                                                                                         "javax.faces.ViewState": self.viewstate2},
                              cookies={'JSESSIONID': self.parent.res.cookies['JSESSIONID'],
                                       'UserSessionFilter.sessionId': self.parent.res2.cookies[
                                           'UserSessionFilter.sessionId']},
                              catch_response=True) as self.res4:

            if "You're almost done" not in self.res4.text:
                self.res4.failure("Got wrong response")
                print(self.res4.text)
            else:
                self.res4.success()
                re3 = re.findall("j_id\d+:j_id\d+", self.res4.text)

                self.viewstate3 = re3[0]

    @task()
    def getinstantquote_2(self):
        with self.client.post("/InsuranceWebExtJS/quote_auto2.jsf", headers=header, data={"autoquote": "autoquote",
                                                                                          "autoquote:age": "0",
                                                                                          "autoquote:gender": "Male",
                                                                                          "autoquote:type": "Excellent",
                                                                                          "autoquote:next.x": "35",
                                                                                          "autoquote:next.y": "7",
                                                                                          "javax.faces.ViewState": self.viewstate3},
                              cookies={'JSESSIONID': self.parent.res.cookies['JSESSIONID'],
                                       'UserSessionFilter.sessionId': self.parent.res2.cookies[
                                           'UserSessionFilter.sessionId']},
                              catch_response=True) as self.res5:

            if "Last Screen" not in self.res5.text:
                self.res5.failure("Got wrong response")
            else:
                self.res5.success()
                re3 = re.findall("j_id\d+:j_id\d+", self.res5.text)

                self.viewstate4 = re3[0]

    @task()
    def getinstantquote_3(self):
        with self.client.post("/InsuranceWebExtJS/quote_auto3.jsf", headers=header, data={"autoquote": "autoquote",
                                                                                          "autoquote:year": "2008",
                                                                                          "makeCombo": "Chrysler",
                                                                                          "autoquote:make": "Chrysler",
                                                                                          "modelCombo": "Aspen",
                                                                                          "autoquote:model": "Aspen",
                                                                                          "autoquote:finInfo": "Own",
                                                                                          "autoquote:next.x": "26",
                                                                                          "autoquote:next.y": "9",
                                                                                          "javax.faces.ViewState": self.viewstate4},
                              cookies={'JSESSIONID': self.parent.res.cookies['JSESSIONID'],
                                       'UserSessionFilter.sessionId':
                                           self.parent.res2.cookies[
                                               'UserSessionFilter.sessionId']},
                              catch_response=True) as self.res6:

            if "Your Instant Quote is" not in self.res6.text:
                self.res6.failure("Got wrong response")
            else:
                self.res6.success()

    @task()
    def stop(self):
        self.interrupt()


class UserBehaviour(TaskSet):

    def on_start(self):
        self.res = self.client.get("/InsuranceWebExtJS/")
        re1 = re.findall("j_id\d+:j_id\d+", self.res.text)
        self.viewstate = re1[0]

        with self.client.post("/InsuranceWebExtJS/index.jsf"
                , data={"login-form": "login-form", "login-form:email": "qamile2@gmail.com"
                    , "login-form:password": "abc123", "login-form:login.x": "57"
                    , "login-form:login.y": "9", "javax.faces.ViewState": self.viewstate}, headers=header,
                              cookies={"JSESSIONID": self.res.cookies["JSESSIONID"]}, catch_response=True) as self.res2:
            if ("Logged in") not in self.res2.text:
                self.res2.failure("User not logged in")
            else:
                print("User logged in")
                self.res2.success()

    tasks = {AutoQuote: 2, AgentLookUp: 1}
    #
    # @task()
    # def testst(self):
    #     print("succ")




class User(HttpUser):
    tasks = [UserBehaviour]
    wait_time = between(5, 10)
    host = "http://demo.borland.com"
