#formats
print(24, 34, 44, 54)
print(24, 34, 44, 54, sep='#')
print(24, 34, 44, 54, sep='#', end="\n")
n1 = 44
name="uber"
print("Score for {} is {}".format(name, n1))

print('{}'.format("format this string"))
fname = "Omkar"
lname = "Dnyanmote"
print("{}.....{}".format(fname, lname))

#use format to allign and give width to output
print(format(fname, "<15s"))
print(format(fname, ">15s"))
print(format(fname, "^15s"))
#fill empty spaces with any character
print(format(fname, "$<15s"))
print(format(fname, "#>15s"))
print(format(fname, "*^15s"))

#use integers with format strings
print("Score is {}".format(8))
print("Score is {:,}".format(88888))
print("Score is {:15,} only".format(888888888))
print("Score is {:<15,} only".format(888888888))
print("Score is {:->15,} only".format(888888888))
print("Score is {:-<15,} only".format(888888888))
print("Score is {:^15,} only".format(888888888))
print("Score is {:-^15,} only".format(888888888))

#integer to binary
number = 10
print("Binary of {0} is {1:b}".format(number, number))
while(number > 0):
    print("Binary of {0} is: {1:b} Octal: {2:o} Hexadecimal: {3:x}" \
        .format(number, number, number, number))
    number -= 1

#use format to access lists and dictionaries
language = ['python', 'django', 'java', 'node']
print("I love to work with ", language[1])
print("I love to work with {}".format(language))
print("I love to work with {0[0]}".format(language))
print("Secure language is {0[2]}".format(language))

friends = {"Mohan": "Chennai", "Yuko": "Japan"}
print("Mohan is from {0[Mohan]} \nYuko is from {0[Yuko]}" \
.format(friends))
