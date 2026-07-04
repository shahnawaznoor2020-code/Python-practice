a=float(input("Enter the length first side of triangle :"))
b=float(input("Enter the length second side of triangle :"))
c=float(input("Enter the length third side of triangle:"))
s=(a+b+c)/2
p=a+b+c
area=(s*(s-a)*(s-b)*(s-c)) ** 0.5
print("The area of the triangle is ",round(area,2))
print("The perimeter of the triangle is ",p)