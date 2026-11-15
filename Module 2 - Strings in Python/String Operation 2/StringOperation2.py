#counting substring from a string
#count()
#string.count(substring)

s1="We are learning Python. Python is fun"
s2="Python"
print(f"Occurance of {s2} is {s1.count(s2)}")

#Changing case of String

s3="Python"
print(s3.upper())
print(s3.lower())
print(s1.title())
print(s1.capitalize())

#Starting and ending with
# startswith()
#string(s1.startswith(substring))
print(s1.startswith("we"))
print(s1.startswith("We"))

print(s1.endswith("n"))
print(s1.endswith("N"))