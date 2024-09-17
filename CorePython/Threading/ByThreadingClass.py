import threading
from threading import *
class Hi(Thread):
        for i in range(1, 15):
            print("Hii...", i)
t1 = Hi()
t1.start()
