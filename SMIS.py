student = {}

def details():
    name = input("Enter the name : ")
    cls = input("Enter the class : ")
    rollno = int(input("Enter the roll no : "))
    age = int(input("Enter the age : "))
    address = input("Enter the address : ")
    state = input("Enter the state : ")
    pincode = int(input("Enter the pincode : "))
    
    student[name] = [rollno, age, cls, address, state, pincode]

def display():
    school = input("Enter the school name : ")
    nametosearch = input("Enter the name of student whose details to be searched : ")
    print(f"\t\t{school}\nName : {nametosearch}\t\tRoll No : {student[nametosearch][0]}\nAge : {student[nametosearch][1]}\t\t\tClass : {student[nametosearch][2]}\nAddress : {student[nametosearch][3]}\t\tState : {student[nametosearch][4]}\nPincode : {student[nametosearch][5]}")

def main():
    n = int(input("Enter the number of the records to be added : "))
    for i in range(1, n + 1):
        details()
    display()

main()
