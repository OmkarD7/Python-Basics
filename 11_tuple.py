sample = ()
print(type(sample))
#sample = (24, 34, 56)
sample = 25, 65, 43
print(sample)
sample = (25, 6, 11, [10, "Omkar", 5.5])
print(sample)
#2D tuple
sample = ((1, 2, 3), (4, 5, 6), (7, 8, 9))
print(sample)
#print element at position 1*1
print(sample[1][1])
#creating tuples from list and sets
scores = [25, 54, 65]
sample = tuple(scores)
print(sample)

scores = {25, 54, 65}
sample = tuple(scores)
print(sample)

#using tuple constructor
onlyOne = "omg"
checkOne = tuple(onlyOne)
print(type(checkOne))
print(checkOne)

#without using tuple constructor
onlyOne = "omg"
checkOne = (onlyOne,)
print(type(checkOne))
print(checkOne)

sample = (25, 6, 11, [10, "Omkar", 5.5], 'a', 8.8, "Dnyanmote")
#(6, 11, [10, 'Omkar', 5.5], 'a', 8.8, 'Dnyanmote')
print(sample[1:])
#(25, 6, 11, [10, 'Omkar', 5.5], 'a', 8.8)
print(sample[:6])
#(25, 11, 'a')
print(sample[:6:2])

#tuple is immutable -> you cannot modify the tuple
#but can assign a new tuple to same variable

sample = (25, 65, 76)
print(sample[0])

#illegal statement
#TypeError: 'tuple' object does not support item assignment
#sample[0] = 33

#this is legal
sample = (44, 66, 45)
print(sample)

#adding tuples
vowel1 = ('a', 'e', 'i',)
vowel2 = ('o', 'u')
vowel = vowel1 + vowel2
print(vowel)

#TypeError: 'tuple' object doesn't support item deletion
#del sample[0]

for item in sample:
    print(item)

#del the given tuple
#del sample