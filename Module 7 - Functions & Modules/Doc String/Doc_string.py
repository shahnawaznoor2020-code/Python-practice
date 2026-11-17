def func():
    """
    This is a docstring
    We can write what a function does
    :return:
    """
    return None
print(func())
print(help(func))

def divide(num1,num2):
    """
    :param num1: a number to be divided
    :param num2: a number to divide
    :return: float if num2 is not zero or str if num2 is not zero
    """
    #doc string must be first and nowhere else
    if num2 == 0:
        return "Cannot divide by zero"
    else:
        return num1/num2
print(divide(6,3))
print(help(divide))
