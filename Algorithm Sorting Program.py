def bubble_sort():
    bubble_list = list_main.copy()
    print("\n\n[1]Ascending")
    print("[2]Descending")
    sel = input('Input choice: ')
    if sel == '1':
        for i in range(6):
            if i == 0:
                print("\n\nOriginal List : ",bubble_list, end = "\n")

            print("\n\nLoop {0}: ".format(i))
            for x in range(5):
                print("{0} > {1} ".format(bubble_list[x],bubble_list[x+1]),end = '')
                if bubble_list[x] > bubble_list[x+1]:
                    temp = bubble_list[x]
                    bubble_list[x] = bubble_list[x+1]
                    bubble_list[x+1] = temp
                    print(bubble_list)
                elif bubble_list[x] <= bubble_list[x+1]:
                    print(bubble_list)
        print("\n\nResult of Ascending Order Bubble Sorting:")
        print(bubble_list)

    elif sel == '2':
        for i in range(6):
            if i == 0:
                print("\n\nOriginal List : ",bubble_list, end = "\n")
            print("\n\nLoop {0}: ".format(i))
            for x in range(5):
                print("{0} < {1}".format(bubble_list[x],bubble_list[x+1]),end = '')
                if bubble_list[x] < bubble_list[x+1]:
                    temp = bubble_list[x]
                    bubble_list[x] = bubble_list[x+1]
                    bubble_list[x+1] = temp
                    print(bubble_list)
                elif bubble_list[x] >= bubble_list[x+1]:
                    print(bubble_list)
        print("\n\nResult of Descending Order Bubble Sorting:")
        print(bubble_list)

def insertion_sort():
    insertion_list = list_main.copy()
    print("\n\n[1]Ascending")
    print("[2]Descending")
    sel = input('Input choice: ')
    if sel == '1':
        print(insertion_list,'\n')
        ctr = 0
        for x in range(1,len(insertion_list)):
            while insertion_list[x] < insertion_list[x-1] and x > 0:
                    print("Loop{0}: {1} < {2}".format(ctr,insertion_list[x],insertion_list[x-1]),end = ' ')
                    temp = insertion_list[x]
                    insertion_list[x] = insertion_list[x-1]
                    insertion_list[x-1] = temp
                    print(insertion_list)
                    ctr+=1
                    if insertion_list[x-1] < insertion_list[x] and x > 0:
                        print("Loop{0}: {1} < {2}".format(ctr,insertion_list[x],insertion_list[x-1]),end = ' ')
                        print(insertion_list)
                    x-=1
                    ctr+=1

        print("\n\nResult of Ascending Order Insertion Sorting:")
        print(insertion_list)

    elif sel == '2':
        print(insertion_list,'\n')
        ctr = 0
        for x in range(1,len(insertion_list)):
            while insertion_list[x] > insertion_list[x-1] and x > 0:
                    print("Loop{0}: {1} > {2}".format(ctr,insertion_list[x],insertion_list[x-1]),end = ' ')
                    temp = insertion_list[x]
                    insertion_list[x] = insertion_list[x-1]
                    insertion_list[x-1] = temp
                    print(insertion_list)
                    ctr+=1
                    if insertion_list[x-1] > insertion_list[x] and x > 0:
                        print("Loop{0}: {1} > {2}".format(ctr,insertion_list[x],insertion_list[x-1]),end = ' ')
                        print(insertion_list)
                    x-=1
                    ctr+=1

        print("\n\nResult of Descending Order Insertion Sorting:")
        print(insertion_list)



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
        menu()

    elif cho == '3':
        insertion_sort()
        menu()

    elif cho == '4':
        print("Blank Option")
        menu()

    elif cho == '5':
        print("Blank Option")
        menu()

    elif cho == '6':
        print("Program End")
        exit()


list_main= [9,5,1,4,3,8]
bubble_list = []
insertion_list = []
item = 1
# while item <= 6:
#     val = int(input("Enter Value {0}: ".format(item)))
#     if val not in list_main:
#         list_main.append(val)
#         item +=1
#     elif val in list_main:
#         print("Same Value in List")
menu()


