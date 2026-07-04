def add(a):
    return a+a
print(add(5))

#syntax
fun= lambda a:a+1
result=fun(2)
print(result)

func=lambda a,b:a+b
print(func(3,4))

#Filter(function,sequence)
seq=[1,2,3,4,5]
even=lambda x:True if x%2==0 else False
filtered_output=filter(even,seq)
print(filtered_output)
print(f"Even number in the sequence are :{list(filter(even,seq))}")


#Map
even=lambda x:True if x%2==0 else False
filtered_output=map(even,seq)
print(filtered_output)
print(f"Map output in the sequence are :{list(map(even,seq))}")

mapped_output=map(lambda x:x**2,seq)
print(mapped_output)
print(f"Map output in the sequence is :{list(mapped_output)}")