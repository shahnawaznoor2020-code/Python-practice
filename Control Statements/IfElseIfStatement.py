#if-elif-......-else
marks=int(input("Enter yours Marks:"))
if 90 <= marks <= 100:
    print("Grade is A+")
elif 80 <= marks <= 90:
    print("Grade is A")
elif 70 <= marks <= 80:
    print("Grade is B")
elif 60 <= marks <= 70:
    print("Grade is C")
elif 50 <= marks <= 60:
    print("Grade is D")
elif 40 <= marks <= 50:
    print("Grade is E")
else:
    print("Grade is F")