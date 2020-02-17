#lists
mixed = [2, 4, 5, 45, 71, "Dnyanmote", "Omkar", 99.99, "uber"]
print(mixed[3])
print(id(mixed))

# : operator
#slice from third index position to (7-1)th position
newslice = mixed[3:7]
print(newslice)
print(type(newslice))

#slice from negative direction
backslice = mixed[-4::-1]
print(backslice)

#iterating through list
for item in mixed:
    print(item)

friends = ["uber", "ola", "zoom", "riderz", "didi"]
firstProviders = [provider[0] for provider in friends]
print(firstProviders)
lengthOfEachItem = [len(provider) for provider in friends]
print(lengthOfEachItem)

#in operator
print("uber" in friends)
print('z' in "Omkar")

#add items in two list
getx = [x for x in 'Omkar']
print(getx)
getx = [x+y for x in 'Omkar' for y in 'Dnyanm']
print(getx)

#creating 2 dimensional list
print("adi "*4)
clone = [4]*3
#[4,4,4]
print(clone)
clone2 = [[4]*3]*3
print(clone2)

#list addition
friends1 = ["Oma", "Oka", "Chia"]
friends2 = ["Pic", "Sic", "Tik"]
print(friends1 + friends2)

#OR
friends1.extend(friends2)
print(friends1)

print(mixed)
print(mixed[0: 6: 2])
#inserting element at given index
mixed.insert(0, 55)
print(mixed)
#poping element of given index
check = mixed.pop(0)
print("popped " + str(check) + " from " + str(mixed))
print(mixed)
#poping last element
mixed.pop()
print(mixed)
#delet elemet
del mixed[0]
print(mixed)

#2D list using for loop
'''
[4]*3 -> range(0,2)
'''
#[[4, 4, 4], [4, 4, 4], [4, 4, 4]]
twoDimension = [[4]*3 for a in range(0,3)]
print(twoDimension)

#[[0, 0, 0], [1, 1, 1], [2, 2, 2]]
twoDimension = [[a]*3 for a in range(0,3)]
print(twoDimension)

#[[0, 0, 0], [1, 1, 1], [4, 4, 4]]
twoDimension = [[a**2]*3 for a in range(0,3)]
print(twoDimension)

#[[0, 0, 0], [1, 1, 1], [8, 8, 8]]
twoDimension = [[a**3]*3 for a in range(0,3)]
print(twoDimension)