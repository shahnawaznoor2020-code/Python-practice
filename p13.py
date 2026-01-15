#reverse
from p6 import language

days_of_week=['mon','tue','wed','thur','fri','sat','sun']
print(days_of_week)
days_of_week.reverse()
print(days_of_week)

#sort
numbers=[4,9,0,8,6,2,3,1,3,5,9,75,21,4,5,4]
print(numbers)
numbers.sort(reverse=True)
print(numbers)

#count
#item_to_count=int(input('Enter item to count: '))
#print(f"Occurence of {item_to_count} is {numbers.count(item_to_count)} ")

#membership - in
language=['python','javascript','java','c']
print(language)
print("python" in language)
print("C++" in language)
print("R" not in language)
print("python" not in language)