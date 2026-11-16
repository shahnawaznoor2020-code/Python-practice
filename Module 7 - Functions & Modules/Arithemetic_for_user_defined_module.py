"""
a simple arithmetic module
"""
def add(a,b):
    return a+b
def squre_root(a):
    return a**(0.5)

print(f"for arithematic.py __name__ is {__name__}")
if __name__=="__main__":
    a = 10
    b = 20
    result = add(a, b)
    print(result)