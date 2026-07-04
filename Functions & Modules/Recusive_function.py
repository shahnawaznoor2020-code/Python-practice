"""
Recursion is a process in which a function calls itself until a condition is met
"""
def factorial(n):
    factorial = 1
    while n > 1:
        factorial *= n
        n -= 1
    return factorial
n=int(input("Enter a number"))
print(f"factorial of {n} is {factorial(n)}")

"""
There are 2 parts to any recursive function
1.Base/Terminal condition
2. Recursive  function
"""
def fact(num):
    if num == 1:
        return 1
    else:
        return num * fact(num-1)
num=int(input("Enter a number"))
print(f"factorial of {num} is {fact(num)}")

#In Python we can pass a function as argument of another function
def add_1(num):
    return num+1
def square(num):
    return num**2
num=int(input("Enter a number"))
print(f"square of {num} is {square(add_1(num))}")
