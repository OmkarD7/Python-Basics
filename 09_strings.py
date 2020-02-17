#strings

name = "umrao jaan"
print('u' not in name)
print(name)
#convert into all capitals
print(name.upper())
#Capotalize first letter
print(name.capitalize())
#in Title format
title =name.title()
print(title)
#Swap between capital and small
print(title.swapcase())
#count of given char in string
print(name.count('a'))
#count of given char in sub-string
print(name.count('a', 0, 5))

#palindrome
str1 = input("Enter the String: ")
str2 = str1[::-1]
print(str1, " ", str2)


