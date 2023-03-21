string = input("Enter the string : ")
u = 0
l = 0
for i in string:
    if i.isupper():
        u += 1
    elif i.islower():
        l += 1
    else:
        pass
print(f"String : {string}")
print(f"Uppercase : {u}")
print(f"Lowercase : {l}")
