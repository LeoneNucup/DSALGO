def bubble_sort():
    print("\n\n[1]Ascending")
    print("[2]Descending")
    sel = input('Input choice: ')
    while sel not in ['1','2']:
        print("Invalid Input")
        sel = input("Input Choice: ")
    if sel == '1':
        bubble_listA = list_main.copy()
        print("BUBBLE SORT : ASCENDING")
        for i in range(6):
            if i == 0:
                print("\n\nOriginal List : ",bubble_listA, end = "\n")

            print("\n\nLoop {0}: ".format(i))
            for x in range(5):
                print("{0} > {1} ".format(bubble_listA[x],bubble_listA[x+1]),end = '')
                if bubble_listA[x] > bubble_listA[x+1]:
                    print(" True ", end = ' ')
                    temp = bubble_listA[x]
                    bubble_listA[x] = bubble_listA[x+1]
                    bubble_listA[x+1] = temp
                    print(bubble_listA)
                elif bubble_listA[x] <= bubble_listA[x+1]:
                    print(" False ", end = ' ')
                    print(bubble_listA)
        print("\n\nResult of Ascending Order Bubble Sorting:")
        print(bubble_listA)

    elif sel == '2':
        bubble_listD = list_main.copy()
        print("BUBBLE SORT : DESCENDING")
        for i in range(6):
            if i == 0:
                print("\n\nOriginal List : ",bubble_listD, end = "\n")
            print("\n\nLoop {0}: ".format(i))
            for x in range(5):
                print("{0} < {1}".format(bubble_listD[x],bubble_listD[x+1]),end = '')
                if bubble_listD[x] < bubble_listD[x+1]:
                    print(" True ", end = ' ')
                    temp = bubble_listD[x]
                    bubble_listD[x] = bubble_listD[x+1]
                    bubble_listD[x+1] = temp
                    print(bubble_listD)
                elif bubble_listD[x] >= bubble_listD[x+1]:
                    print(" False ", end = ' ')
                    print(bubble_listD)
        print("\n\nResult of Descending Order Bubble Sorting:")
        print(bubble_listD)


def selection_sort():
    print("\n\n[1]Ascending")
    print("[2]Descending")
    sel = input('Input choice: ')
    while sel not in ['1','2']:
        print("Invalid Input")
        sel = input("Input Choice: ")
    if sel == '1':
        selection_listA = list_main.copy()
        length = len(selection_listA)
        print("SELECTION SORT : ASCENDING")
        print("Unsorted List: ", selection_listA, end = " ")
        for initial in range(length-1):
            minIndex = initial
            for i in range(initial+1, length, 1):
                if selection_listA[i] < selection_listA[minIndex]:
                    minIndex = i
            ##FOR LABEL
            if selection_listA[minIndex] < selection_listA[initial]:
                print("Switch {0} and {1}".format(selection_listA[initial],selection_listA[minIndex]))
            elif selection_listA[minIndex] == selection_listA[initial]:
                print("No changes for {0}".format(selection_listA[initial]))

            temp = selection_listA[initial]
            selection_listA[initial] = selection_listA[minIndex]
            selection_listA[minIndex] = temp
            print("Loop {0}".format(initial),selection_listA, end = " ")
        print("Sorted List")
    if sel == '2':
        selection_listD = list_main.copy()
        length = len(selection_listD)
        print("SELECTION SORT : DESCENDING")
        print("Unsorted List: ", selection_listD, end = " ")
        for initial in range(length-1):
            maxIndex = initial
            for i in range(initial+1, length, 1):
                if selection_listD[i] > selection_listD[maxIndex]:
                    maxIndex = i

            ##FOR LABEL
            if selection_listD[maxIndex] > selection_listD[initial]:
                print("Switch {0} and {1}".format(selection_listD[initial],selection_listD[maxIndex]))
            elif selection_listD[maxIndex] == selection_listD[initial]:
                print("No changes for {0}".format(selection_listD[initial]))

            temp = selection_listD[initial]
            selection_listD[initial] = selection_listD[maxIndex]
            selection_listD[maxIndex] = temp
            print("Loop {0}".format(initial),selection_listD, end = " ")
        print("Sorted List")


def insertion_sort():
    print("\n\n[1]Ascending")
    print("[2]Descending")
    sel = input('Input choice: ')
    while sel not in ['1','2']:
        print("Invalid Input")
        sel = input("Input Choice: ")
    if sel == '1':
        insertion_listA = list_main.copy()
        size = len(insertion_listA)
        print("INSERTION SORT : ASCENDING")
        print(" Current unsorted list\n ",insertion_listA,"\n")
        for out in range(size-1):
            for i in range(out, -1,-1): # TO COMPARE ITEM VALUE FROM RIGHT TO LEFT
                if insertion_listA[i+1] < insertion_listA[i]:
                    print("Loop{0}: {1} < {2} TRUE".format(out, insertion_listA[i+1], insertion_listA[i]),end=" ")
                    print(insertion_listA)
                    temp = insertion_listA[i+1]
                    insertion_listA[i+1] = insertion_listA[i]
                    insertion_listA[i] = temp
                else:
                    print("Loop{0}: {1} < {2} FALSE".format(out, insertion_listA[i+1], insertion_listA[i]))
                    break

            print(" Current sorted list\n Loop {0}:".format(out),insertion_listA, "\n")

    elif sel == '2':
        insertion_listD = list_main.copy()
        size = len(insertion_listD)
        print("INSERTION SORT : DESCENDING")
        print(" Current unsorted list\n ",insertion_listD,"\n")
        for out in range(size-1):
            for i in range(out, -1,-1): # TO COMPARE ITEM VALUE FROM RIGHT TO LEFT
                if insertion_listD[i+1] > insertion_listD[i]:
                    print("Loop{0}: {1} > {2} TRUE".format(out, insertion_listD[i+1], insertion_listD[i]),end=" ")
                    print(insertion_listD)
                    temp = insertion_listD[i+1]
                    insertion_listD[i+1] = insertion_listD[i]
                    insertion_listD[i] = temp
                else:
                    print("Loop{0}: {1} > {2} FALSE".format(out, insertion_listD[i+1], insertion_listD[i]))
                    break

            print(" Current sorted list\n Loop {0}:".format(out),insertion_listD, "\n")


def menu():
    print("\n\n-----Menu-----")
    print("[1]Bubble Sort")
    print("[2]Selection Sort")
    print("[3]Insertion")
    print("[4]...")
    print("[5]...")
    print("[6]Exit")
    cho = input("Input Choice: ")
    while cho not in ['1','2','3','4','5','6']:
        print("Invalid Input")
        cho = input("Input Choice: ")
    option(cho)

def option(cho):
    if cho == "1":
        bubble_sort()
        menu()
    elif cho == '2':
        selection_sort()
        menu()

    elif cho == '3':
        insertion_sort()
        menu()

    elif cho == '4':
        menu()

    elif cho == '5':
        menu()

    elif cho == '6':
        print("Program End")
        exit()


list_main= []
bubble_listA = []
bubble_listD = []
selection_listA = []
selection_listD = []
insertion_listA = []
insertion_listD = []
item = 1
while item <= 6:
    val = int(input("Enter Value {0}: ".format(item)))
    if val not in list_main:
        list_main.append(val)
        item +=1
    elif val in list_main:
        print("Same Value in List")
menu()


