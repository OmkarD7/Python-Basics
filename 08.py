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
