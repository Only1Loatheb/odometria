import time
class Timer():
    def __init__(self, t):
        self.target = t
        self.time_prev = time.time()
    def sleep(self):
        time_now = time.time()
        time_delta = time_now - self.time_prev
        self.time_prev = time_now
        if time_delta < self.target:
            time.sleep(self.target - time_delta)