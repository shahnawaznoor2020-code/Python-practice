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

#if-elif-......-else
marks=int(input("Enter yours Marks:"))
if 90 <= marks <= 100:
    print("Grade is A+")
elif 80 <= marks <= 90:
    print("Grade is A")
elif 70 <= marks <= 80:
    print("Grade is B")
elif 60 <= marks <= 70:
    print("Grade is C")
elif 50 <= marks <= 60:
    print("Grade is D")
elif 40 <= marks <= 50:
    print("Grade is E")
else:
    print("Grade is F")

#Nested if
if marks>=40:
    print("Congratulation! You passed the exam ")
    if 90 <= marks <= 100:
        print("Grade is A+")
    elif 80 <= marks <= 90:
        print("Grade is A")
    elif 70 <= marks <= 80:
        print("Grade is B")
    elif 60 <= marks <= 70:
        print("Grade is C")
    elif 50 <= marks <= 60:
        print("Grade is D")
    elif 40 <= marks <= 50:
        print("Grade is E")
else:
    print("Sorry, Better Luck Next time!")

#ternary operator
#true -expression if condition else false condition
print("Even") if num%2==0 else print("Odd")