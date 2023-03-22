stack = []

def push(s):
    e = input("Enter the element to be added in the stack : ")
    s.append(e)
    print(f'Stack updated...!!!')

def pop(s):
    e = s.pop()
    print(f'Element removed : {e}')

def show(s):
    print(f'Stack is : {s}')

while True:
    print("P:PUSH    O:POP    S:SHOW    Q:QUIT")
    ch = input("Enter the choice : ").upper()
    if ch == "P":
        push(stack)
    elif ch == "O":
        pop(stack)
    elif ch == "S":
        show(stack)
    elif ch == "Q":
        break
    else:
        print("Invalid input...!!!")
