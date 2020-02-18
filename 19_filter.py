'''
Filter
It works on iterable
works with two parameters
1. function name/ lambda
2. Iterable
Function named/lambda will evaluate for each item in iterable.
Map-> It will return list created by lambda function
Filter-> It will return the list for which lambda/named function evaluates to True
'''

numbers = [55, 45, 65, 85, 22, 15, 5, 88, 78]
selected = filter(lambda a: a>45, numbers)
print(list(selected))

evenNumbers = filter(lambda a: a%2 == 0, numbers)
print(list(evenNumbers))

oddNumbers = filter(lambda a: a%2 != 0, numbers)
print(list(oddNumbers))

alphabets = ['a', 'b', 'c' ,'d' , 'e' , 'f', 'g', 'h', 'i']
vowels = ['a', 'e', 'i', 'o', 'u']
checkVowels = filter(lambda alpha: alpha in vowels, alphabets)
print(list(checkVowels))

