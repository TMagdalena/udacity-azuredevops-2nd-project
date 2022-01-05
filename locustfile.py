from locust import HttpLocust, TaskSet, task

class MyTaskSet(TaskSet):
  @task
  def index(self):
    self.client.get("/posts")
    
  @task
  def users(self):
    self.client.post("/posts", json=
        {
        "CHAS":{
            "0":0
        },
        "RM":{
            "0":6.575
        },
        "TAX":{
            "0":296.0
        },
        "PTRATIO":{
            "0":15.3
        },
        "B":{
            "0":396.9
        },
        "LSTAT":{
            "0":4.98
        }
        })

class MyLocust(HttpLocust):
  task_set = MyTaskSet
  
