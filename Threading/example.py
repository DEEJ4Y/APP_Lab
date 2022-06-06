import threading
import time


class app1(threading.Thread):
    def run(self):
        for i in range(5):
            print("thread 1")
            time.sleep(1)


class app2(threading.Thread):
    def run(self):
        for i in range(5):
            print("thread 2")
            time.sleep(1)


t1 = app1()
t2 = app2()

t1.start()
t2.start()
