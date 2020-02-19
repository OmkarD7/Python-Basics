import time
import multiprocessing

def getSqaure(numList,ress):
    
    print(numList)
    print(ress)
    for index, n in enumerate(numList):
        print(index, " ", n)
        ress[index] = n*n
    print("Result in process1: ",list(ress))

#print("Result list: ", result)
#this line is mandatory
if __name__ == '__main__':
    numbers = [1,2,3,4,5]
    #datatype and size
    #data to be shared between different processes
    result = multiprocessing.Array('i', 5)
    print("Result List in Main Process Before: ", list(result))
    process1 = multiprocessing.Process(target=getSqaure, args=(numbers,result))

    process1.start()

    process1.join()
    print("Result in main: ", list(result))
    print("Done with multiprocessing !!")