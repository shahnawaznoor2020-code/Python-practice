name="John"
age=20
language="Python"
hours=3

#John is 20 years old. He studies Python 3 hours a day
print(name,"is",age,"years old. He studies ",language,hours,"hours a day")
print(f"{name} is {age} years old. He studies {language} {hours} hours a day")

sub1=78
sub2=87
sub3=91
print(f"{name} scored {sub1+sub2+sub3} marks in test")
percentage=(sub1+sub2+sub3)/3
print(f"{name} scored {round(percentage,2)}% marks in test")