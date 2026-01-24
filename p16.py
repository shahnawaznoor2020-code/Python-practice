#Module 7
t1 = ("Python", 10, 1.5, True, [1, 2, 3], None, (10, 20))
print(t1)
print(len(t1))

#Accesing items of a tuple
print(t1[0])
print(t1[-1])

#(  ) are optional
t1 = 1, 2, 7,3, 4, 5,2,2
print(type(t1))
print(t1.index(7))
print(t1.count(2))

l1=[1,2,3,4,5]
print(type(l1))
t2=tuple(l1)
print(type(t2))

#funtions are Same as list but tuple cannot be editted

#Memory location
ppp=213
print(id(ppp))