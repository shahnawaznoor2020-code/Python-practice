#Slicing of list
l1=[3,4,8,1,0,4,9,7,3,6]
print(l1)
print(l1[1:6:1])

#Concatination
l2=[2,3,7]
l3=[0,4]
print(l2+l3)
print(l3+l2)

#Repeation -*
print(l3*3)

#Append
#adds only one element at the back of list
fruits=['apple','banana','orange']
print(fruits)
fruits.append('mango')
print(fruits)
#append does not return any list it only updates existing list


#insert
#adds an element before the specified index
fruits.insert(2,'Guvava')
print(fruits)
