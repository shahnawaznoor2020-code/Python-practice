pr=int(input("Enter Principal Amount :"))
r=int(input("Enter Rate of Interest in p.a. :"))
t=int(input("Enter Time :"))
si=(pr*r*t)/100
total=pr+si
print("Simple interest is :",si)
print("Total Amount",total)