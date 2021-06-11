import time
from locust import HttpUser, task, between

class QuickstartUser(HttpUser):
    wait_time = between(1,2.5)

    @task
    def hello_world(self):
        self.client.get("")
        self.client.get("1/results/")
        self.client.post("1/vote/", {"choice":1})

    def on_start(self):
        pass
