import threading
import Queue

class synchronizedQueue :
    def __init__(self) :
        self.lock = threading.Lock()
        self.queue = Queue.Queue()
    def put(self, e) :
        self.lock.acquire()
        self.queue.put(e)
        self.lock.release()
    def get(self) :
        self.lock.acquire()
        ret = None if self.queue.empty() else self.queue.get()
        self.lock.release()
        return ret

class synchronizedOutput : 
    def __init__(self) :
        self.lock = threading.Lock()
    def out(self, string) : 
        self.lock.acquire()
        print string
        self.lock.release()

