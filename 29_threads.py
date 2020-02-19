import threading
import time

def callMeForEachThread(threadname, delay):
    counter = 0
    while counter <=10:
        print("Thread Name: ",threadname, " with counter value: " ,counter)
        time.sleep(delay)
        counter += 1

thread1 = threading.Thread(target=callMeForEachThread, args=("Thread1", 1))
thread2 = threading.Thread(target=callMeForEachThread, args=("Thread2", 3))

thread1.start()
thread2.start()

thread1.join()
thread2.join()

print("Multithreading finished !!!")