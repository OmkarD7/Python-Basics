import time
import multiprocessing

sqresult = []
curesult = []
def getSqaure(numList,ress):
    print("Calculate square of numbers")
    for n in numList:
        time.sleep(2)
        ress.append(n*n)
        print("Temporary Result List in process 2: ",ress)
        print("Square of ",n,": ",n*n)
    print("Result in process 1: ",ress)

def getCube(numList, resc):
    print("Calculate cube of numbers")
    for n in numList:
        time.sleep(2)
        resc.append(n*n*n)
        print("Temporary Result List in process 2: ",resc)
        print("Cube of ",n,": ",n*n*n)
    print("Result in process 2: ",resc)

print("Result list of square: ", sqresult)
print("Result list of cube: ",curesult)
#this line is mandatory
if __name__ == '__main__':
    numbers = [1,2,3,4,5]

    process1 = multiprocessing.Process(target=getSqaure, args=(numbers,sqresult))
    process2 = multiprocessing.Process(target=getCube, args=(numbers,curesult))

    process1.start()
    process2.start()

    process1.join()
    process2.join()

    print("Done with multiprocessing !!")
    #processes we are running and the main process will have different memory bank
    #so the results in process1 and process 2 won't appear in main process
    #for transfering results from MB of one process into MB of another IPC(Inter Process Communication) is used
    print("Result sq in main: ", sqresult)
    print("Result cube in main: ",curesult)