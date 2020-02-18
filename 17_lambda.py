'''
noname or anonymous function
'''

def addNum(n1, n2):
    return n1 + n2

sum = addNum(4,2)
print(sum)

#lamda way
#does not work on multiple statment functions
#cannot/no need to use return 
sum = lambda n1, n2: n1 + n2
print(sum(3,5))

message = lambda m: print(m)
print(message("Hello World!"))

square = lambda n: n*n
print(square(5))

#list of lambda functions (functions in collection)
lambdaList = [lambda a: a**2, lambda a,b: a*b, lambda a,b: a+b]
print(lambdaList[0](6))
print(lambdaList[1](6,4))
print(lambdaList[2](6,6))

#lambda without any parameter ->there has to be something to return
noparacheck = lambda: True
print(noparacheck())
print(type(noparacheck()))