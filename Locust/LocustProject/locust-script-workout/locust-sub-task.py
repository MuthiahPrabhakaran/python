from locust import task, HttpUser, TaskSet


class Home(TaskSet):
    @task()
    def home(self):
        print("I am in home page")
        print("Parent token "+self.parent.token)

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
    def add_to_cart(self):
        print("I am in cart section")
        self.schedule_task(Cart, first=True)

    @task()
    def stop(self):
        self.interrupt(reschedule=False)


class Cart(TaskSet):
    @task()
    def apply_promo_code(self):
        print("Apply promo code")

    @task()
    def remove_product(self):
        print("Remove the product")

    @task()
    def payment(self):
        print("I am in payment page")

    @task()
    def stop(self):
        self.interrupt(reschedule=False)


class Behaviour(TaskSet):
    def on_start(self):
        print("User log in")
        self.token = "dummy token"

    # tasks = [Home, ViewProduct, Cart]
    tasks = {Home: 5, ViewProduct: 4}

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
