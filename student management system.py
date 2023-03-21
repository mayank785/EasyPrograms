markList = []

def main():
    print("1. Adding marks of new student : ")
    print("2. Insertion of marks at desired postition")
    print("3. Append list of new students to main list")
    print("4. Modify marks of exisiting student")
    print("5. Delete marks by position")
    print("6. Delete marks by values")
    print("7. Sort list in ascending order")
    print("8. Sort list in descending order")
    print("9. Display the final marks")

    ch = int(input("Enter the position : "))
    
    if ch == 1:
        add_marks()
    elif ch == 2:
        insert_marks()
    elif ch == 3:
        append_list()
    elif ch == 4:
        modify_list()
    elif ch == 5:
        delete_by_position()
    elif ch == 6:
        delete_by_value()
    elif ch == 7:
        sort_asc()
    elif ch == 8:
        sort_desc()
    elif ch == 9:
        display()
        
    main()

def add_marks():
    marks = int(input("Enter Marks : "))
    markList.append(marks)
    print("Marks added successfully !")

def insert_marks():
    marks = int(input("Enter Marks : "))
    position = int(input("Enter position : "))
    markList.insert(position, marks)
    print("Marks added successfully !")

def list_maker():
    l = []
    limit = int(input("Enter the limit : "))
    for i in range(1, limit + 1):
        val = int(input("Enter Value : "))
        l.append(val)
        return l
    
def append_list():
    list_maker()
    markList.extend(l)
    print("New list appended to main list successfully !")

def modify_list():
    n = int(input("Enter the position of the value : "))
    if n < len(modify_list):
        old = markList[n]
        new = int(input("Enter the new value : "))
        markList[n] = new
        print("Value updated successfully !")

def delete_by_position():
    n = int(input("Enter the position of the record to  be deleted : "))
    if n < len(markList):
        e = markList.pop(n)
        print(f'Element {e} removed successfully !')
    else:
        print("Invalid position")

def delete_by_value():
    val = int(input("Enter the value to be deleted : "))
    if val in markList:
        e = markList.remove(val)
        print(f'Element {e} removed successfully !')
    else:
        print("Value not found")

def sort_asc():
    markList.sort()
    print("List sorted in ascending order !")

def sort_desc():
    markList.sort(reverse = True)
    print("List sorted in descending order !")

def display():
    print(markList)

main()
