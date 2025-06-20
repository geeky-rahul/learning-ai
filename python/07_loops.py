# Question 1: Counting positive numbers
# numbers = [1,-2,3,-4,5,6,-7,-8,9,10]
# positive_numbers = 0
# for number in numbers:
#     if number>0:
#         positive_numbers += 1
# print(positive_numbers)


# Question 2: Sum of even numbers upto given number n
# n = 6
# sum = 0
# for num in range(1, n+1):
#     if num % 2 == 0:
#         sum += num
# print(sum)


# Question 3: table of 10, but skip the fifth itration
# for num in range(1,11):
#     if num == 5:
#         continue
#     print('10', 'x', num, '=', num*10)
    
    
# Question 4: Reverse a string using loop
# name = "rahul"
# reversed_name = ""
# for char in name:
#     reversed_name = char + reversed_name
# print(reversed_name)
    

# Question 5: Given string, find first non-repeated character
# str = "teeter"
# for char in str:
#     if str.count(char) == 1:
#         print("char is:", char)
#         break


# Question 6: calculate factorial of a number using while loop
# num = 5
# factorial = 1
# while num > 0:
#     factorial *= num
#     num -= 1
# print(factorial)


# Question 7: Keep asking the user for input until they enter a number between 1 and 10
# while True:
#     user_input = int(input("Enter a number b/w 1 and 10: "))
#     if 1 <= user_input <= 10:
#         print("Thanks")
#         break
#     else:
#         print("Invalid number, try again")


# Question 8: Check if a number is prime
# number = 8
# is_prime = True
# if number > 1:
#     for num in range(2, number):
#         if number % num == 0:
#             is_prime = False
#             break
# print(is_prime)


# Question 9: check if all elements in a list are unique. If a duplicate is found, exit the loop and print the duplicate.
# items = ["apple", "banana", "orange", "apple", "mango"]
# unique_item = set()
# for item in items:
#     if item in unique_item:
#         print("Duplicate item is: ", item)
#     unique_item.add(item)


# Question 10: Implement an exponential backoff strategy that doubles the wait time between retries, starting from 1 second, but stops after 5 retries.
import time

wait_time = 1
max_retries = 5
attempts = 0

while attempts < max_retries:
    print("Attempt", attempts + 1, "-wait time", wait_time)
    time.sleep(wait_time)
    wait_time *= 2
    attempts += 1