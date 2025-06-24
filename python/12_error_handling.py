file = open('test_1.txt', 'w')

try:
    file.write("this is my first txt file")
finally:
    file.close()
    
    
# new Syntax for above
with open('test_2.txt', 'w') as file:
    file.write("this is my second txt file") # No need to close the file in this syntax it is inbuild in "with"
