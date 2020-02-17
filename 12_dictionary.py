newDict = {}
print(type(newDict))

#any type of key is possible except float 
newDict = {"Monday":"mon", 2:"tue", 'W':"wed", 4:"thur", "friends":["Omi", "Dnyanmote"]}
print(newDict)

#create dictionary from list of tuples
friends = dict([("chennai",8),("mumbai",7),("pune", 3)])
print(friends)

#retrieve the value
print(friends["pune"])
print(friends.get("mumbai"))

#update the dictionary
friends.update({'mumbai': 18})
print(friends)

#iterate through dictionary
for key, value in friends.items():
    print(key, " ", value)

#create dictionary where key is string 
#and value is length of string from the list of strings
friends = ['amar', 'akbar', 'anthony', 'tiger']
#somedict = {'amar':4, 'akbar':5, 'anthony':6, 'tiger':5}
somedict = {value:len(value) for value in friends}
print(somedict)