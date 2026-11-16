countries=["India","USA","Japan","China","Ireland","Iceland","Ira","sri lanka"]
output=[]
count=0
for country in countries:
    if country[0]=='I':
        count=count+1
print(count)
for country in countries:
    if country.startswith("i"):
        count=count+1
        output.append(country)
print(count)
print(output)