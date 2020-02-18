'''
if expresssion:
    pass
if condition:
    pass
else:
    pass
'''

number = int(input("Input number: "))
if (number > 30):
    print("number is greater than 30")
else:
    print("number is smaller")

numbers = [1,2,3,4,5,6,7,8,9,10]
if (number in numbers):
    print("present")
else:
    print("absent")

friends1 = ["Ola", "Uber", "Didi", "Mave", "ride"]
friends2 = ["ride", "jia", "Didi", "zoom"]
for f1 in friends1:
    if f1 in friends2:
        print("Common Friend: ",f1)
    
