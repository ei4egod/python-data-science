# 1 - lists
# ordered, mutable

odds = [5,7,9]
sum(odds)
total = 0
for num in odds:
    total = total + num
    # total += num

total = 0
for i, num in enumerate(odds):
    total = total + (i*num)

sq_roots = [n**0.5 for n in odds]
cube_roots = [n**(1/3) for n in odds]
divis_by_five = [n for n in range(31) if n%5 ==0]

list(map(lambda x: x+1, odds))
list(filter(lambda n: n < 5, [3,4,5,6]))

# lambda is an inline function, two arguments, iterable on right, function on left
# list comprehension can have an if conditional
# map does not have an 'if'
# filter can have an 'if'

reduce(lambda total, n: total + n, odds)
reduce(lambda total, n: total + n, odds, 10)

# with the third argument, 10 is initialized into total, then summation occurs


# 2 - tuple
# ordered, immutable

tup1 = (3,4)

# 3 - sets
# unordered, unique, iterable, mutable, only takes immutable/hashable values

s1 = {3,4}


# 4 - dicts
# no order, iterable, keys are unique, keys are hashable(immutable)

d = {}
for n in range(5):
    d[n] = n**2

d.get(5)
d.get(5,0)
