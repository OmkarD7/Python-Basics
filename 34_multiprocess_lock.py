import multiprocessing
import time

def depositeMoney(money, lp):
    for i in range(10):
        #lock acquired
        lp.acquire()
        money.value += 1
        #lock released
        lp.release()
        print("Deposited!!")

def withdrawMoney(money, lp):
    for i in range(5):
        #lock acquired
        lp.acquire()
        money.value -= 1
        #lock released
        lp.release()
        print("Withdrawn!!")


if __name__ == "__main__":
    lockProcess = multiprocessing.Lock()
    #shared resource
    balanceMoney = multiprocessing.Value('i', 0)
    process1 = multiprocessing.Process(target=depositeMoney, args=(balanceMoney,lockProcess))
    process2 = multiprocessing.Process(target=withdrawMoney, args=(balanceMoney,lockProcess))

    process1.start()
    process2.start()

    process1.join()
    process2.join()

    print("Final Balance: ", balanceMoney.value)