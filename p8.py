from xml.sax.handler import version

from p6 import language

s1="Python is fun"
print(s1[0])
print(s1[-1])
print(len(s1))

language="Python"
version="3.13.4"
print(language+version)

print(s1*3)

#Membership
print("Python" in s1)
print("i" in s1)
print("python" in s1)
print("z" in s1)
print("python" not in s1)

#Comparison in string
print("python" == "Python")
print("Python " == "Python")

#Removing spaces from a string - strip
s2="       Python  "
print(s2.strip() == "Python")

#Replace()
s3="We are learning python"
print(s3)
print(s3.replace("Python","Java"))
print(s3)
print(s3.replace("e","E",1))
print(s3.replace("ef","E"))