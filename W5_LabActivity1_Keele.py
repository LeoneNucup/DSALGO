## Keele, Regine Ann G.

stack = []

def menu():
    print("""Menu:
[1] Push
[2] Pop
[3] Exit
""")
    answer = input("Enter Choice: ")
    while answer not in ['1','2','3']:
            print("Invalid Input")
            answer = input("Enter Choice: ")
            choice = int(answer)
    choice = int(answer)
    while choice >=0 and choice <=3:
        if choice == 1:
            push()
            print()
            menu()
        if choice == 2:
            pop()
            print()
            menu()
        if choice == 3:
            exit()

def push():
    print("\n===============PUSH===============")
    item = input("Input item to push: ")
    if len(stack) <=4:
        stack.append(item)
    else:
        print("Stack reached overflow")
        print()
        menu()
    top= len(stack)-1
    print("Top Item: ", stack[top])
    print("Top index: ", top)
    print("Stack items: ")
    for i in range(len(stack)-1, -1, -1):       
        print(stack[i])
        

def pop():
    print("\n===============POP===============")
    print("Pop Item: ", stack.pop())
    if len(stack) != 0:
        top= len(stack)-1
        print("Top index: ", top)
        print("Stack items: ")
        for i in range(len(stack)-1, -1, -1):       
            print(stack[i])
    else:
        print("Stack reached underflow")
        print()
        menu()
    

menu()
