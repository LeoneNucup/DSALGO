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

    choice = int(input("Input Option : "))
    options(choice,maxq,deq)

def options(choice,maxq,deq):
    while choice not in [1,2,3]:
        print("Invalid Input")
        choice = int(input("Input Option : "))

    if choice == 1 and maxq <= 4:
        print("-"*15+"ENQUEUE"+"-"*15)
        add = input("Input Item to add in the queue : ")
        queue.append(add)
        print("Front Item : " + queue[0])
        print("Front Index : " + str(deq))
        print("Rear Item : " + queue[maxq])
        print("Rear Index : ", maxq)
        print("Queues : ", queue)
        if maxq <5:
            maxq+=1
        menu(maxq,deq)
    elif choice == 1 and maxq == 5:
        print("-"*15+"Limit Exceeded"+"-"*15)
        menu(maxq,deq)

    elif choice == 2 and deq <= 4:
        deq+=1
        print("-"*15+"DEQUEUE"+"-"*15)
        print("First item in the queue to remove : " + str(queue.pop(0)))

        if len(queue) == 0:
            print("QUEUE EMPTY")
            deq+=1
            menu(maxq,deq)
        print("Front Item : " + str(queue[0]))
        print("Front Index : " + str(deq))
        print("Rear Item : " + str(queue[-1]))
        print("Rear Index : ", str(maxq-1))
        print("Queues : ", queue , "\n")

        menu(maxq,deq)

    elif choice == 2 and deq == 5:
        print("-"*15+"QUEUE EMPTY"+"-"*15)
        menu(maxq,deq)



    elif choice == 3:
        exit()




while maxq <= 4 and deq <= 4:
    menu(maxq,deq)
