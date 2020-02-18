#use filter and lambda to get list of palindromes only
names = ["madam", "malayalam", "peep", "chick", \
"Amore", "Roma", "daga"]
#using reversed
palinNames = filter(lambda a: a == ("".join(reversed(a))), names)
print(list(palinNames))

#using slice
palinNames = filter(lambda a: a == a[::-1], names)
print(list(palinNames))