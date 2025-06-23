# Question 1: write a decorator that measures the time of a function takes to excute
import time

def timer(func):
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        print(f"{func.__name__} ran in {end-start} time")
        return result
    return wrapper

@timer  # python understand it like: example_function = timer(example_function)
def example_function(n):
    time.sleep(n)    
example_function(2)
    

# Question 2: Create a decorator to print the function name and the values of its arguments every time the function is called 
def debug(func):
    def wrapper(*args, **kwargs):
        args_value = ', '.join(str(arg) for arg in args)
        kwargs_value = ', '.join(f"{k}={v}" for k, v in kwargs.items())
        print(f"{func.__name__} with args {args_value} and kwargs {kwargs_value}")
        return func(*args, **kwargs)
    return wrapper

@debug
def hello():
    print("hello")

@debug
def greet(name, greetng = "Hello"):
    print(f"{greetng} {name}")
    
hello()
greet("rahul")

# Question 3: Implement a decorator that caches the return values of a function, so that when it called with the same arguments, the chached value is returned instead of re-excuting the function
def cache(func):
    cache_value = {}
    print(cache_value)
    def wrapper(*args):
        if args in cache_value:
            return cache_value[args]
        result = func(*args)
        cache_value[args] = result
        return result
    return wrapper
        
@cache
def long_running_function(a,b):
    time.sleep(4)
    return a + b

print(long_running_function(2,3))
print(long_running_function(2,3))
print(long_running_function(4,3))