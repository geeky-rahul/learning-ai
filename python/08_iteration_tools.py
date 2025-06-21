f = open('python\README.md')
print(f.readline())
print(f.__next__) # raw method
# iter(f) is f # True

# open and read files using for loop
for line in open('README.md'):
    print(line, end='')
    
# open and read files using for loop
while True:
    line = f.readline()
    if not line: break
    print(line, end='')
    
test0= "Rahul"
if not test0:
    print("kuch bhi")
    
test1 = ""
if not test1:
    print("kuch bhi")
 
# iteration on list   
my_list = [1,2,3,4]
i = iter(my_list)
# iter(my_list) is my_list # False
print(i.__next__()) # or i.next()
print(i.__next__())
print(i.__next__())
print(i.__next__())
# print(i.__next__()) # StopIteration


# iteration on dict
D = {'a': 1, 'b': 2}
for key in D.keys():
    print(key)