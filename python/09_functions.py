# Question 1: write a function to calculate and return the square of a number.
def square(number): # number is a parameter
    print(number**2)  
result = square(4)
print(result) # Output None
    
def square(number): 
    return number**2  
result = square(4)
print(result)
    

# Question 2: Two numbers as a parameter and returns their sum
def sum_num(a,b):
    return a+b
print(sum_num(2,4))


# Question 3: Polymorphism in functions
# Write a function multiplies two numbers, but can also accept and multiply strings.
def multiply(a,b):
    return a*b
print(multiply(5,2))
print(multiply("rahul",5))


# Question 4: Function that returns both the area and circumference of a circle given its radius.
def circle_stats(radius):
    circumference = 2*3.14*radius
    area = 3.14*radius**2
    return circumference, area
print(circle_stats(3))


# Question 5: Default parameter
def greet(name = "Rahul"):
    return "Hello " + name + "!"
print(greet())


# Question 6: create a lambda function to compute the cube of a number
cube = lambda x: x**3
print(cube(3))
    

# Question 7: Function with *args, write a function that takes variable number of arguments and returns their sum
def sum_all(*args):
    return sum(args)
print(sum_all(2,3,4))


# Question 8: Function with **kwargs, Create a function that accepts any number of keyword arguments and prints them in the format key: value
def print_kwargs(**kwargs):
    for key, value in kwargs.items():
        print(f"{key}: {value}")
print_kwargs(name= "Rahul", course = "software development", age = 20)


# Question 9: Write a generator function that yields even numbers up to a specified limit
# def even_generator(limit):
#     for i in range(2, limit+1, 2):
#         return i  # error
# for num in even_generator(10):
#     print(num)

def even_generator(limit):
    for i in range(2, limit+1, 2):
        yield i  
for num in even_generator(10):
    print(num)


# Question 10: create a recursive function to calculate the factorial of a number
def factorial(n):
    if n == 0:
        return 1
    else: 
        return n*factorial(n-1)
print(factorial(5))