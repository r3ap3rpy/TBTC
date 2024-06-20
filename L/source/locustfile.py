from locust import HttpUser, task
import time
class HelloWorldUser(HttpUser):
    @task
    def hello_world(self):
        self.client.get("/hello")
        self.client.get("/world")

    @task
    def view_items(self):
        for i in range(10):
            self.client.get(f"/items?id={i}", name = "/items")
            time.sleep(.5)

    @task 
    def view_users(self):
        for i in range(5):
            self.client.post(f"/user/{i}", name = "/user")
            time.sleep(.5)
