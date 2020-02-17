#sets
number_set = {5, 2, 6, 4, 8}
print(number_set)

#error- TypeError: unhashable type: 'list'
#mixed_type = {4,5,6,[7,8,9]}
# #list cannot be item in a set but tuple can be used as an item in set
mixed_type = {4, 5, 6, 7, (55, 44, 33)}
print(mixed_type)

#converting list into set
number_list = [4, 5, 7, 8, 8, 9]
number_set = set(number_list)
print(number_set)

#adding item to set
number_set.add(12)
print(number_set)

#removing item from set
#will throw key error if item is not present in the set
number_set.remove(12)
print(number_set)

#discard
#will not throw any error if item is not present in the set
number_set.discard(100)
print(number_set)

#pop item from set
#throws error if set is empty
print(number_set.pop())

#clear will remove all the itemns in the set
number_set.clear()
print(number_set)

#frozen set
freeze = frozenset(number_set)
#cannot modify the frozen set
# AttributeError: 'frozenset' object has no attribute 'add'
#freeze.add(33)

#unions and intersections
score1 = {55, 67, 88, 99}
score2 = {54, 67, 87, 99}
print(score1)
print(score2)
print(score1.union(score2))
print(score1.intersection(score2))

#substraction/difference
#those elements of score1 which are not in score2
print(score1 - score2)
#those elements of score2 which are not in score1
print(score2 - score1)