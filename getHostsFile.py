import os
import sys
import socket
import threading

from lib import synchronizedOutput, synchronizedQueue

class myThread(threading.Thread) :
    def __init__(self, queue, output) :
        threading.Thread.__init__(self)
        self.queue = queue
        self.output = output
    def run(self) :
        while True :
            cur = self.queue.get()
            if (cur == None) : break
            try :
                result = socket.getaddrinfo(cur, None)
                self.output.out(result[0][4][0] + '\t' + cur)
            except : pass

if len(sys.argv) != 2 :
    print sys.argv[0] + ' <Input File>'
else :
    q = synchronizedQueue()
    out = synchronizedOutput()
    f = file(sys.argv[1])
    for line in f.readlines() :
        q.put(line[ : -1])
    threads = list()
    for i in range(0, 5) :
        t = myThread(q, out)
        t.start()
        threads.append(t)
    for t in threads :
        t.join()
