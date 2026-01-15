#Sets are non-sequential collection of items
#comma separated element enclosed within {}

set1={10,"Python",2.5}
print(set1)
print(type(set1))

#Indexing and Slicing are not allowed

#length of the set
print(len(set1))

#Sets do not allow duplicate

l1=[10,2.5,10,30,10]
print(l1,type(l1))
l2={10,2.5,10,30,10}
print(l2,type(l2))

nums={1,2,3,0,-1}

#Membership operator
print(0 in nums)
print(10 in nums)

#concatination and repetition cannot be done set

weekdays=('Mon','Tue','Wed','Thur','Fri','Sat','Sun')
weekday=set(weekdays)
print(weekday)

sets1={1,2,3,0,-1}
print(sets1)

#Add
sets1.add(5)
print(sets1)

#Remove gives error if element are not present
sets1.remove(5)
print(sets1)

#Discard if element are not present no error are given
sets1.discard(5)

student_1={"English","Maths","Physics","Chemistry","Computer Science"}
student_2={"English","Biology","Physics","Chemistry"}
student_3={"Sanskrit","Maths","Computer Science"}

print(student_1)
print(student_2)

# common subjects of student 1 and student 2
common_subjects= student_1.intersection(student_2)
print(common_subjects)
common_subjects=student_1 & student_2
print(common_subjects)
common_subjects=student_3 & student_2

#All the subjects of student and student 2
all_subjects=student_1.union(student_2,student_3)
print(all_subjects)
all_subjects=student_1 | student_2 | student_3
print(all_subjects)

#difference of sets
s=student_1-student_2
print(s)
s=student_2.difference(student_1)
print(s)

#Symmetric Difference
s=student_1.symmetric_difference(student_2)
print(s)

s1={1,2,3,0}
s1.add(-1)
print(s1)

#Frozen sets - Immutable sets
fs1=frozenset({10,20,30})
print(fs1,type(fs1))

fs2=frozenset({100,200,2,30,50})

print(fs1 & fs2)
print(fs1 | fs2)
print(fs1 - fs2)