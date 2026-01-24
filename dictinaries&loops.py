user={
    "username":"my_username",
    "password":"test@123",
    "email":"my_user@example.com",
    "address":"ABC road ,11111111",
    "country":"Australia",
}
sensetive_info=["password","address","Phone"]
for i in sensetive_info:
    if i in user:
        user.pop(i)
    else:
        print(f"{i} is not present in user")
print(user)