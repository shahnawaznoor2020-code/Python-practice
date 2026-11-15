#list inside a list
l1=[5,1.2,"Python",True,None,[1,2,3],10]

print(l1)
print(l1[-2][0])

l2=[[1,2],[3,4],[5,6,[0,1]]]
print(len(l2))
print(l2[-1])
print(l2[-1][-1])
print(l2[-1][-1][-1])