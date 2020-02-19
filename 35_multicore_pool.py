from multiprocessing import Pool
import time

def myFunction(numList):
    counter = 0
    for i in range(1000):
        counter = i * i
    return counter

if __name__ == "__main__":
    t1 = time.time()
    pool = Pool()
    pool.map(myFunction, range(100))
    pool.close()
    pool.join()

    print ("Time taken by pool: ",time.time()- t1)

    t2 = time.time()
    result = []
    for i in range(1000):
        result.append(myFunction(i))
    print ("Time taken by serial processing: ",time.time()- t2)