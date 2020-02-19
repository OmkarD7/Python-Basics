import threading
import time


def getSqaure(numList):
    print("Calculate square of numbers")
    for n in numList:
        time.sleep(1)
        print("Square of ",n,": ",n*n)

def getCube(numList):
    print("Calculate cube of numbers")
    for n in numList:
        time.sleep(2)
        print("Cube of ",n,": ",n*n*n)

numbers = [1,2,3,4]

#single threaded execution
getSqaure(numbers)
getCube(numbers)

#multi threaded execution
thread1 = threading.Thread(target=getSqaure, args=(numbers,))
thread2 = threading.Thread(target=getCube, args=(numbers,))

thread1.start()
thread2.start()

thread1.join()
thread2.join()

print("Done with Maths !! Exhausted NOW !!")