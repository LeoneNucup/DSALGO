def bubble_sort():
    print("\n\n[1]Ascending")
    print("[2]Descending")
    sel = input('Input choice: ')
    if sel == '1':
        for i in range(6):
            print("\n\nLoop {0}: ".format(i))
            for x in range(5):
                if main_list[x] > main_list[x+1]:
                    temp = main_list[x]
                    main_list[x] = main_list[x+1]
                    main_list[x+1] = temp
                    print(main_list)
                elif main_list[x] <= main_list[x+1]:
                    print(main_list)
        print("\n\nResult of Ascending Order Bubble Sorting:")
        print(main_list)

def menu():
    print("\n\n-----Menu-----")
    print("[1]Bubble Sort")
    print("[2]Selection Sort")
    print("[3]...")
    print("[4]...")
    print("[5]Exit")
    cho = input("Input Choice: ")
    while cho not in ['1','2','3','4','5']:
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
        print("Blank Option")
        menu()

    elif cho == '4':
        print("Blank Option")
        menu()

    elif cho == '5':
        print("Program End")
        exit()


main_list= []
bubble_list = []
item = 1
while item <= 6:
    val = int(input("Enter Value {0}: ".format(item)))
    if val not in main_list:
        main_list.append(val)
        item +=1
    elif val in main_list:
        print("Same Value in List")
menu()


