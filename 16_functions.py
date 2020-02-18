'''
def funname(parameter list)
    pass


'''
def customMessage(message):
    print(message)

customMessage("Hello!")

startNumber = int(input("Enter the start number"))
endNumber = int(input("Enter the end number"))


def calculateTotal(number1, number2):
    total = 0
    while (number1 != (number2 + 1)):
       total += number1
       number1 += 1
       print(total)  
calculateTotal(startNumber, endNumber)


#using recursion
def addAll(num1, num2):
    if num2 != 0:
        return num2 + addAll(num1, num2-1)
    else:
        return 0
print(addAll(startNumber,endNumber))
