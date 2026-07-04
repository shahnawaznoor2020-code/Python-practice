#Syntax of if
#indentation
# if condition
#     statement 1
#     statement2
# statement n

age=int(input("What is your age :"))
if age>=18:
    print("Congratulations! You are an Adult. You can now cast vote!!!!")
print("Rest of Program")

# if-else
# if condition
#     #block of code to be executed when condition is true
# else
#     #block of code to be executed when condition is false

if age>=18:
    print("Congrats! You can cast vote!!!")
else:
    print("Sorry, you are not allowed to cast vote!!!")
print("Rest of Program")

#program to print check if integer is odd or even
num=int(input("Enter a number:"))
if num%2==0:
    print(num,"is an even number")
else:
    print(num,"is an odd number")

#to print if a number is positive or negative
ne=int(input("Enter a Integer:"))
if ne>=0:
    print(ne,"is an positive number")
else:
    print(ne,"is an negative number")




