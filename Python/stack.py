# WAP to add and remove elemens from stack
a = []
while True:
    print("1. Push")
    print("2. Pop")
    print("3. Show Stack")
    print("4. Exit")

    ch = int(input("Enter your choice: "))
    if ch == 1:
        data = int(input("Enter data: "))
        a.append(data)
    elif ch == 2:
        if len(a) == 0:
            print("Stack is empty")
        else:
            print("Popped element is", a.pop())
    elif ch == 3:
        print('Stack is:',a)
    elif ch == 4:
        break
    else:
        print("Invalid choice")
