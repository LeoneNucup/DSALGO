# KEELE , REGINE
# NUCUP, LEONE
# CS-201

queue = []
maxq = 0
deq=0
def menu(maxq,deq):

    print()
    print("""MENU:\n
    [1] Enqueue
    [2] Dequeue
    [3] Exit
    """"\n")

    answer = input("Input Option : ")
    while answer not in ['1','2','3']:
        print("Invalid Input")
        answer = input("Input Option : ")
    choice = int(answer)
    options(choice,maxq,deq)

def options(choice,maxq,deq):
    if choice == 1 and maxq <= 4:
        print("-"*15+"ENQUEUE"+"-"*15)
        add = input("Input Item to add in the queue : ")
        queue.append(add)
        print("Front Item : " , (queue[0]))
        print("Front Index : " , (deq))
        print("Rear Item : " , queue[-1])
        print("Rear Index : ", maxq)
        print("Queues : ", queue)
        if maxq <5:
            maxq+=1
        menu(maxq,deq)
    elif choice == 1 and maxq == 5:
        print("-"*15+"Limit Exceeded"+"-"*15)
        menu(maxq,deq)

    elif choice == 2 and len(queue) >1:
        deq+=1
        print("-"*15+"DEQUEUE"+"-"*15)
        print("First item in the queue to remove : " , (queue.pop(0)))
        print("Front Item : " , (queue[0]))
        print("Front Index : " ,(deq))
        print("Rear Item : " , (queue[-1]))
        print("Rear Index : ", (maxq-1))
        print("Queues : ", queue , "\n")
        menu(maxq,deq)

    elif choice == 2 and len(queue) == 1:
        print("-"*15+"DEQUEUE"+"-"*15)
        print("First item in the queue to remove : " ,(queue.pop(0)))
        print("-"*15+"Queue Empty"+"-"*15)
        menu(maxq,deq)

    elif choice == 2 and len(queue) == 0:
        print("-"*15+"DEQUEUE"+"-"*15)
        print("-"*15+"Queue Empty"+"-"*15)
        menu(maxq,deq)

    elif choice == 3:
        exit()

while maxq <= 4:
    menu(maxq,deq)
