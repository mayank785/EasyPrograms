emp = {}

n = int(input("Enter the number of records : "))

for i in range(1, n + 1):
    name = input("Enter name : ")
    salary = int(input("Enter salary : "))
    emp[name] = salary

print("Name\tSalary")

for i in emp:
    print(i, "\t", emp[i])
