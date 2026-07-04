s1="Hello World"
for char in s1:
    print(char)
print("End of the loop")
#same for tuple

employee={'name':'John','age':22,'salary':200}
print(employee)
for emp in employee:
    print(emp,employee[emp])
for emp in employee.items():
    print(emp)

#range() - built-in function used to generate sequence of integer in a given integer range
#range(start,stop,step)

#for i in range(start,stop,step):
    #statement

for i in range(1,12,1):
    print(i)
for i in range(1,12,2):
    print(i)
for i in range(2,10,2):
    print(i)
for i in range(20,10,-2):
    print(i)
for i in range(10,0,-1):
    print(i)
print("Happy New Year")

groceries=['apple','banana','mango']
for index in range(len(groceries)):
    print(groceries[index],index)


totals=0
scores=[2,45,102,4,9,12,45,90,1,0,1]
highest=scores[0]
lowest=scores[0]
for i in scores:
    if i<lowest:
        lowest=i
    if i>highest:
        highest=i
    totals=totals+i
print(totals)
total=sum(scores)
print(total)
print(lowest)
print(highest)
highes=max(scores)
lowes=min(scores)
print(lowes)
print(highes)