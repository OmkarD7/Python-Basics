#integer
n1 = 5
print(str(n1) + " is of type " + str(type(n1)))

#float
n2 = 6.2
print(str(n2) + " is of type " + str(type(n2)))

#lists
mixed = []
print(type(mixed))
mixed = [2, 5.5, 'a', 'B', "uber", "Omkar"]
print(type(mixed))
print(mixed)
#value at specific index
print("character at index 3 is: "+ str(mixed[3]))
#length of list
print("length of list is: "+ str(len(mixed)))

#tuple
nochange = ()
print(type(nochange))
nochange = (2, 5.5, 'a', 'B', "uber", "Omkar")
print(nochange)
print(nochange[0])
#below statement is illegal for tuple
#nochange[0] = 4

#strings
location = "Chennai !!"
multiline = '''
            Hello
            How are you
            '''
print(location)
print(type(location))
print(len(location))
print(location[0])
print(multiline)
print(type(multiline))

#sets
noorder = {25, 35, 45, 80, 90}
print(noorder)
print(type(noorder))
#subscription is not possible in set so following statement is illegal
#print(noorder[0])

#dictionary
keyvalue = {}
keyvalue = { 1:"Omkar", "Tech":"python", 4:8, 9:"ML" }
print(keyvalue)
print(type(keyvalue))
print(keyvalue[1])
print(keyvalue["Tech"])

#type conversion
n2 = 5
print(n2)
print(type(n2))

n3 = float(n2)
print(n3)
print(type(n3))

n4 = str(n3)
print(n4)
print(type(n4))

#input - everything is string in input
score1 = input("Inputs for score 1: ")
score2 = input("Inputs for score 2: ")
print("Score is: " + score1 + score2)
print("##################################")
score1 = int(input("Inputs for score 1: "))
score2 = int(input("Inputs for score 2: "))
print("Score is: " + str(score1 + score2))
#no need of conversion into string while using ','
print("Score is: " , (score1 + score2))
