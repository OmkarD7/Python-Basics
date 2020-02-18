'''for loop'''
print("for loop of string")
vowels = "aeiou"
for v in vowels:
    print(v)

numbers = [1,2,3,4,5,6,7,8,9,10]
total = 0
for n in numbers:
    total += n
print("\nfor loop of list")
print("Total is {}".format(total))

#using for loop with range
print("\nusing for loop with range")
for n in range(1,5):
    print(n)
for n in range(1,10):
    print(n, end=" ")
print()
for n in range(1,10,2):
    print(n, end=" ")

#for else loop
#statements under else will only execute if the for loop is complete
print("\n\nfor else loop")
for n in numbers:
    print(n**n)
else:
    print("Exponent for all numbers is done!")
    
#else statement would not be executed as for loop is breaking in betwween
for n in numbers:
    print(n**n)
    if n == 7:
        break
else:
    print("Exponent for all numbers is done!")