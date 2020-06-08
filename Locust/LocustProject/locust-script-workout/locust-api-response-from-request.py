from locust import HttpUser, SequentialTaskSet, between, task
import re

header = {
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,"
              "application/signed-exchange;v=b3",
    "Accept-Encoding": "gzip, deflate, br",
    "Accept-Language": "en-US,en;q=0.9",
    "Connection": "keep-alive",
    "Host": "demo.borland.com",
    "Sec-Fetch-Mode": "navigate",
    "Sec-Fetch-Site": "same-origin",
    "Sec-Fetch-User": "?1",
    "Upgrade-Insecure-Requests": "1",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) "
                  "Chrome/77.0.3865.120 Safari/537.36 "
}


class UserBehaviour(SequentialTaskSet):

    def on_start(self):
        global res
        res = self.client.get("/InsuranceWebExtJS/")
        re1 = re.findall("j_id\d+:j_id\d+", res.text)
        global viewstate
        viewstate = re1[0]

        global res2
        with self.client.post("/InsuranceWebExtJS/index.jsf"
                , data={"login-form": "login-form", "login-form:email": "qamile2@gmail.com"
                    , "login-form:password": "abc123", "login-form:login.x": "57"
                    , "login-form:login.y": "9", "javax.faces.ViewState": viewstate}, headers=header,
                              cookies={"JSESSIONID": res.cookies["JSESSIONID"]}, catch_response=True) as res2:
            if ("Logged in") not in res2.text:
                res2.failure("User not logged in")
            else:
                res2.success()

    @task
    def choose_service_autoquote(self):
        with self.client.get("/InsuranceWebExtJS/quote_auto.jsf", cookies={'JSESSIONID': res.cookies['JSESSIONID'],
                                                                           'UserSessionFilter.sessionId': res2.cookies[
                                                                               'UserSessionFilter.sessionId']},
                             headers=header,
                             catch_response=True) as res3:

            if "Get Instant Auto Quote" not in res3.text:
                res3.failure("Got wrong response")
            else:
                res3.success()
                re2 = re.findall("j_id\d+:j_id\d+", res3.text)
                global viewstate2
                viewstate2 = re2[0]
                print("viewstate2" + viewstate2)

    @task
    def getinstantquote_1(self):
        with self.client.post("/InsuranceWebExtJS/quote_auto.jsf", headers=header, data={"autoquote": "autoquote",
                                                                                         "autoquote:zipcode": "00000000",
                                                                                         "autoquote:e-mail": "qamile2@gmail.com",
                                                                                         "autoquote:vehicle": "car",
                                                                                         "autoquote:next.x": "38",
                                                                                         "autoquote:next.y": "10",
                                                                                         "javax.faces.ViewState": viewstate2},
                              cookies={'JSESSIONID': res.cookies['JSESSIONID'],
                                       'UserSessionFilter.sessionId': res2.cookies[
                                           'UserSessionFilter.sessionId']},
                              catch_response=True) as res4:

            if "You're almost done" not in res4.text:
                res4.failure("Got wrong response")
                print(res4.text)
            else:
                res4.success()
                re3 = re.findall("j_id\d+:j_id\d+", res4.text)
                global viewstate3
                viewstate3 = re3[0]

    @task
    def getinstantquote_2(self):
        with self.client.post("/InsuranceWebExtJS/quote_auto2.jsf", headers=header, data={"autoquote": "autoquote",
                                                                                          "autoquote:age": "0",
                                                                                          "autoquote:gender": "Male",
                                                                                          "autoquote:type": "Excellent",
                                                                                          "autoquote:next.x": "35",
                                                                                          "autoquote:next.y": "7",
                                                                                          "javax.faces.ViewState": viewstate3},
                              cookies={'JSESSIONID': res.cookies['JSESSIONID'],
                                       'UserSessionFilter.sessionId': res2.cookies[
                                           'UserSessionFilter.sessionId']},
                              catch_response=True) as res5:

            if "Last Screen" not in res5.text:
                res5.failure("Got wrong response")
            else:
                res5.success()
                re3 = re.findall("j_id\d+:j_id\d+", res5.text)
                global viewstate4
                viewstate4 = re3[0]

    @task
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
                                                                                          "javax.faces.ViewState": viewstate4},
                              cookies={'JSESSIONID': res.cookies['JSESSIONID'],
                                       'UserSessionFilter.sessionId': res2.cookies[
                                           'UserSessionFilter.sessionId']},
                              catch_response=True) as res6:

            if "Your Instant Quote is" not in res6.text:
                res6.failure("Got wrong response")
            else:
                res6.success()


class User(HttpUser):
    tasks = [UserBehaviour]
    wait_time = between(5, 10)
    host = "http://demo.borland.com"
