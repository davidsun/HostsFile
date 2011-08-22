import os
import sys
import threading

from lib import synchronizedOutput, synchronizedQueue

class myThread(threading.Thread) :
    def __init__(self, name, queue, output) :
        threading.Thread.__init__(self)
        self.name = name
        self.queue = queue
        self.output = output
    def getFileName(self) :
        return self.name + '.out'
    def run(self) :
        while True :
            cur = self.queue.get()
            if (cur == None) :
                break
            os.system('ping -c 1 -W 5 ' + cur + ' > ' + self.getFileName())
            fin = file(self.getFileName())
            for l in fin.readlines() :
                loc1 = l.find('(')
                loc2 = l.find(')')
                if (loc1 != -1 and loc2 != -1) :
                    self.output.out(l[loc1 + 1 : loc2] + '\t' + cur)
                break
        os.system('rm ' + self.getFileName())

if len(sys.argv) != 2 :
    print sys.argv[0] + ' <Input File>'
else :
    q = synchronizedQueue()
    out = synchronizedOutput()
    f = file(sys.argv[1])
    for line in f.readlines() :
        q.put(line[ : -1])
    threads = list()
    for i in range(0, 10) :
        t = myThread(i, q, out)
        t.start()
        threads.append(t)
    for t in threads :
        t.join()
