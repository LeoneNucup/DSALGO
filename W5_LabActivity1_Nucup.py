#LEONE NUCUP
stack = []

def menu():
    print("{0:>30}".format("MENU"))
    print("{0:>15}".format("[1] : Push"))
    print("{0:>14}".format("[2] : Pop"))
    print("{0:>15}".format("[3] : Exit"))
    cho = int(input("{0:>40}".format("Enter Choice : ")))
    if cho == 1:
        push()
    elif cho == 2:
        pop()
    elif cho == 3:
        exit()
    else:
        print("Invalid Value ")
        menu()

def push():
    print("-"*30+"PUSH"+"-"*30)
    val = input("Input item to push: ")
    if len(stack) <=5:
        stack.append(val)
        menu()
    elif len(stack) == 6:
        print("Stack Overflow")
        menu()


def pop():
    print("-"*30+"POP"+"-"*30)
    if len(stack) ==0:
        print("Stack underflow")
        menu()
    print("Item popped : ", stack.pop())
    if len(stack) != 0:
        for i in range(len(stack)):
            print(stack[i],end=" ")
        menu()
    elif len(stack) ==0:
        print("Stack underflow")
        menu()




menu()
