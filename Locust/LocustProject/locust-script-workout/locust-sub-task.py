from locust import task, HttpUser, TaskSet


class Home(TaskSet):
    @task()
    def home(self):
        print("I am in home page")

    @task()
    def stop(self):
        self.interrupt(reschedule=False)


class ViewProduct(TaskSet):
    @task()
    def view_product(self):
        print("I am in view product page")

    @task()
    def read_review(self):
        print("read review")

    @task()
    def stop(self):
        self.interrupt(reschedule=False)


class Cart(TaskSet):
    @task()
    def cart(self):
        print("I am in cart page")

    @task()
    def stop(self):
        self.interrupt(reschedule=False)


class Behaviour(TaskSet):
    def on_start(self):
        print("User log in")

    # tasks = [Home, ViewProduct, Cart]
    tasks = {Home: 5, ViewProduct: 4, Cart: 3}

    @task(2)
    def contact_us(self):
        print("I am in contact page")

    @task(1)
    def about_us(self):
        print("I am in about us page")


class Tasks(HttpUser):
    tasks = [Behaviour]
    host = ""
    min_wait = 1000
    max_wait = 10000
