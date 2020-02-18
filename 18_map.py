'''
Map will work only on iterables
It will return list created by lambda function
lambda function works on parameter of map
'''

messages = ['Help', 'Run', 'Fight', 'Request']
for m in messages:
    print("Current message is: ", m)

def printMessage(msg):
    return "Message from function is ", msg

mapcheck = map(printMessage, messages)
print(list(mapcheck))

#working with map and lambda
mapcheck = map(lambda m: "Message from lambda map: "+m, messages)
newlist = (list(mapcheck))
print(newlist)
print(list(mapcheck))
#mapcheck becomes empty after type check as list constructor is being used

scores1 = [25, 35, 45]
scores2 = [10, 15, 20]
scores3 = [2, 3, 4]

#scores4 = sum of each respective item at respective index position
#in scores1 and scores2 multiplied by scores3

scores4 = map(lambda n1, n2, n3: \
    (n1 + n2)*n3, scores1, scores2, scores3)
print(list(scores4))

#consider scenario with list of different length!
#It will only take stable values that are available and calculate the output for them
scores1 = [25, 35, 45, 20, 70]
scores2 = [25, 10, 20, 30]
scores3 = [2, 3, 4]

#scores4 = sum of each respective item at respective index position
#in scores1 and scores2 multiplied by scores3

scores4 = map(lambda n1, n2, n3: \
    (n1 + n2)*n3, scores1, scores2, scores3)
print(list(scores4))


messages = ['Help', 'Run', 'Fight', 'Request']
#create a 2d list of characters in messages with lambda
mapcheck = map(lambda m: list(m), messages)
mylist = (list(mapcheck))
print(mylist)

#without using lambda
mapcheck = map(list, messages)
mylist = list(mapcheck)
print(mylist)