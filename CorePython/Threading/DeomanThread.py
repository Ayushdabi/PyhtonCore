import threading
import time

def first_thread():
    print("Hello Ram")

    for i in range(20):
     time.sleep(100)
     print("How are you Ram?")

def second_thread():
    print("Hello Shyam")
    for i in range(20):
     time.sleep(8)
     print("how are you Shyam?")

t1 = threading.Thread(target=first_thread, daemon='true')
t2 = threading.Thread(target=second_thread)

t1.start()
time.sleep(2)
t2.start()