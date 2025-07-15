import threading

class ConcurrentHandler:
    def __init__(self, manager):
        self.manager = manager #reference for the print_queue_manager(enqueue_job)
        self.lock = threading.Lock() # thread safe, i.e prevents racing of printing jobs meant to happen at the same time.

    #submitting thread safe jobs
    def submit(self,user_id,job_id,priority):

        with self.lock:

            self.manager.enqueue_job(user_id,job_id,priority)