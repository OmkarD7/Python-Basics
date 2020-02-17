
lengthOfList = input("Enter the length of the list: ")
allNumbers = []
for item in range(int(lengthOfList)):
    allNumbers.insert(item, int(input("Enter the number: ")))
print(allNumbers)
start = int(input("Enter the start point of slicing: "))
stop = int(input("Enter the stop point of slicing: "))
slicedList = allNumbers[(start-1):stop]
print(slicedList)
n = len(slicedList)
for i in range(n):
    for j in range(0, n-i-1):
        if slicedList[j] > slicedList[j+1]:
            slicedList[j], slicedList[j+1] = slicedList[j+1], slicedList[j] 
print ("Sorted list is: ")
print(slicedList)

