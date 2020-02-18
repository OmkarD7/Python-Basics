'''
Reduce -> Aggregator functions!
1. It works with iterable
2. It will return single value

'''
from functools import reduce
numbers = [1,2,3,4,5]
total = reduce(lambda num1, num2: num1+num2, numbers)
print(total)

numbers = [55, 45, 65, 85, 22, 15, 5, 88, 78]
largest = reduce(lambda num1, num2: num1 if num1 > num2 else num2, numbers)
print(largest)

smallest = reduce(lambda num1, num2: num1 if num1 < num2 else num2, numbers)
print(smallest)

