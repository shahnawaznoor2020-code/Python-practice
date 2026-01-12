pr=float(input("Enter the Principal Amount:"))
r=float(input("Enter the Rate of Interest in p.a. :"))
t=float(input("Enter the Time :"))
Amount=pr*((1+(r/100))**t)
ci=Amount-pr
print("Compound Interest is :",round(ci,2))
print("Total Amount :",round(Amount,2))
