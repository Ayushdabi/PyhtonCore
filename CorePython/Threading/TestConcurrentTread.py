'''import threading


def my_thread(name):
    for i in range(500):
        print(i, 'Hello ', name)


t1 = threading.Thread(target=my_thread, args=("Ram",))
t2 = threading.Thread(target=my_thread, args=("Shyam",))
t1.start()
t2.start()'''

import threading
import time

def task1():
    for i in range(5):
        print("Task 1 running...")
        time.sleep(1)

def task2():
    for i in range(5):
        print("Task 2 running...")
        time.sleep(1)

# Creating threads
thread1 = threading.Thread(target=task1)
thread2 = threading.Thread(target=task2)

# Starting threads
thread1.start()
thread2.start()

# Waiting for threads to complete
thread1.join()
thread2.join()
