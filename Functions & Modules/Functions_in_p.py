# def Function_name(0 to n no of arguments):
#     set statement

def greeting(name):
    print(f"Hello, {name} good morning!")
    print("It's a beautiful day")

#calling function
greeting("Latita")
greeting("Mark")
greeting("John")

#oddd /  eeven
def even_odd(num):
    if num % 2 == 0:
        print(f"{num} is even")
        return "Even"
    else:
        print(f"{num} is odd")
        return "Odd"
even_odd(5)
even_odd(6)
even_odd(7)
even_odd(8)

def add(num1, num2):
    result1= num1 + num2
    print(f"{num1} + {num2} = {result1}")
    add = num1 + num2
    diff = num1 - num2
    multiply = num1 * num2
    return add, diff, multiply
add(1, 2)
add(3, 4)

#Returning value of a function
print(even_odd(5))
print(even_odd(6))
print(even_odd(7))
print(add(1, 2))
print(add(3, 4))

def arithmetic(num1, num2):
    add1 = num1 + num2
    sub1 = num1 - num2
    multiply = num1 * num2
    return add1, sub1, multiply
val1=int(input("enter first number"))
val2=int(input("enter second number"))

result1, result2, result3 = arithmetic(val1, val2)
print(f"Addition ={val1} + {val2} = {result1}")
print(f"Subtraction ={val1} - {val2} = {result2}")
print(f"Multiplication ={val1} * {val2} = {result3}")

#types of argument
#positional argument - passing the argument in order of their position
#artithmetic()

#default argument
def addd(num1, num2=10):
    result2= num1 + num2
    return result2
print(addd(1, 2))
print(addd(3))
#the non default arguments should not follow the default argument

#keyword argument
def adddd(num1, num2=14 ,num3=10):
    print(f"a={num1}, b= {num2} ,c={num3}")
    return num1 + num2 + num3
result = adddd(1, num3=2)
print(result)

#variable argument in python
def addi(*args):
    result=sum(args)
    print(type(args))
    return result
print(addi(1,2,3,4))

def student_details(sid,sname,*marks):
    print(sid,sname,marks)
    percentage=sum(marks)/len(marks)
    print(f"{sname} with id {sid} secured {percentage}%")
student_details(101,"John",87.5,24,99,78,55,89)

#variable length keywords argument
# **kwargs - variable length keyword argument
def func(**kwargs):
    print(kwargs,type(kwargs))
func(x=10,y=20)
func()

def students_details(sidd,ssname,*extra,**markss):
    if len(markss)==0:
        print(f"{ssname} with id {sidd} did not attend exam")
        print(f"{ssname} does {extra}")
    else:
        percentages=sum(markss.values())/len(markss)
        print(f"{ssname} with id {sidd} secured {percentages}%")
        print(f"{ssname} does {extra}")
        print(markss)
students_details(101,"John",'Football',sub1=78.5,sub2=88,sub3=89)
students_details(102,"May",'Tennis','debate',sub1=78.5,sub2=86,sub3=89,sub4=88,sub5=89)
