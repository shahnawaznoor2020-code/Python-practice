#comma separated key-valued pairs enclosed within {}
#{key1:value1 ,key2:value2 , ........}

groceries={'milk':60,'biscuit':20,'rice':90,'bread':30}
print(groceries)
print(type(groceries))
print(len(groceries))

print(groceries['milk'])
print(groceries['rice'])

#Dictionary are mutable
#updates new key value into the dictionary
#does not have index
groceries['bread']=20
print(groceries)

#adds new key value into the dictionary
groceries['eggs']=10
print(groceries)

marks={'Maths':80.5,'English':76,'Physics':89}
print(marks)
#fetch marks for phy
print(marks['Maths'])

#get() - no error if key not present
print(marks.get('Maths'))
print(marks.get('Chemistry'))
#if key not present default value can be returned
print(marks.get('Chemistry',40))

#membership - check only for key not value
print('Maths' in marks)

#update a dictionary
sem1_marks={'Maths':80.5,'English':76,'Physics':89}
sem2_marks={'Maths':81,'Chemistry':40,'Biology':85}
sem1_marks.update(sem2_marks)
print(sem1_marks)

#pop()
print(groceries)
groceries.pop('milk')
print(groceries)

#python reads dictionary from left to right and reads the most recent value

#not allowed keys - lists,sets,dictionary - mutable data type
#allowed keys - strings,integer,floats,boolean,tuple - immutable data type
#keys of a dictionary can only be immutable
#values can be any data type
d1={'id':1001,'name':"John",'marks':{'Maths':80.5,'English':76,'Physics':89}}
print(d1['marks'])

d2={'id':1001,'name':"John",'marks':[80,98,75]}
print(d2['marks'][1])

#fetch the keys
#keys()
print(d1.keys(),type(d1.keys()))
#values()
print(d1.values(),type(d1.values()))
#items
print(d1.items(),type(d1.items()))