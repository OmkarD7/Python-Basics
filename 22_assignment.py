from functools import reduce

#find the sum of squares of all numbers less than 10
numbers = [5, 6, 11, 12]
sum = reduce(lambda a,b:a+b, map(lambda a:a*a, filter(lambda n: n <= 10, numbers)))
print("sum of squares of all numbers which are less than 10: ",sum)
#other way without using lambda
def fun1(a, b):
    return a+b
def fun2(c):
    return c*c
def fun3(d):
    if d<10:
        return True
    else:
        return False
sum = reduce(fun1, map(fun2,filter(fun3, numbers)))
print("sum of squares of all numbers \
which are less than 10 \
without using lambda function: ", sum)

#find the sum of square of all even numbers
sum = reduce(lambda n1,n2:n1+n2, map(lambda n:n*n, filter(lambda n: n%2 ==0, numbers)))
print("sum of squares of all even numbers: ",sum)
