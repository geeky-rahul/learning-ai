x = 2
y = 3
z = 4
print((x+y)*z)
print(x,y,z)

print(bin(32))
print(oct(32))
print(hex(32))

# or
print(int('1001001', 2)) # for Binary

import math
print(math.floor(20.32))

import random
print(random.random()) # Give random Number between 0 to 1
print(random.randint(1,10))  # Randint = Random integer (1,10) between 1 to 10

l1 = ['a','b','c','d','e']
print(random.choice(l1)) # Randomly choose a element from the list l1
random.shuffle(l1) # Shuffled the list l1
print(l1)

# Sets
setone = {1,2,3,4}
print(setone & {1,3,5}) # intersection of set
print(setone | {1,4,6}) # union of set
print(setone-{1,2,3,4}) # output is set() not {} because empty braces consider as dict
