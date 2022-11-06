def mergeSortup(ascendinglist):
    print("Splitting",ascendinglist)
    if len(ascendinglist)>1:
        mid = len(ascendinglist)//2
        left = ascendinglist[:mid]
        right = ascendinglist[mid:]

        print("Sublist" , left)
        print("Sublist", right)

        mergeSortup(left)
        mergeSortup(right)

        i=j=k=0

        while i < len(left) and j < len(right):
            if left[i] < right[j]:
                ascendinglist[k]=left[i]
                i+=1
            else:
                ascendinglist[k]=right[j]
                j+=1
            k+=1

        while i<len(left):
            ascendinglist[k] = left[i]
            i+=1
            k+=1


        while j<len(right):
            ascendinglist[k] = right[j]
            j+=1
            k+=1
        print("Merging",ascendinglist)


def mergeSortdown(descendinglist):
    print("Splitting",descendinglist)
    if len(descendinglist)>1:
        mid = len(descendinglist)//2
        left = descendinglist[:mid]
        right = descendinglist[mid:]

        print("Sublist" , left)
        print("Sublist", right)

        mergeSortdown(left)
        mergeSortdown(right)
        i=j=k=0

        while i < len(left) and j < len(right):
            if left[i]  > right[j]:
                descendinglist[k]=left[i]
                i+=1
            else:
                descendinglist[k]=right[j]
                j+=1
            k+=1

        while i<len(left):
            descendinglist[k] = left[i]
            i+=1
            k+=1


        while j<len(right):
            descendinglist[k] = right[j]
            j+=1
            k+=1
        print("Merging",descendinglist)



def menu(list_main):
    if len(list_main)==0:
        item=1
        while item <=8:
            val = int(input("Enter {} Value : ".format(item)))
            if val not in list_main:
                list_main.append(val)
                item+=1
            elif val in list_main:
                print("Error, value is not unique")

    print("""
Sort in:
    [a] Ascending
    [b] Descending
    [c] Exit
    """)
    cho= input("Enter Option: ")
    while cho not in ['a','b','c']:
        cho= input("Enter Option: ")

    ascendinglist=list_main.copy()
    descendinglist = list_main.copy()
    if cho == 'a':
        print("Ascending Merge Sort: ")
        mergeSortup(ascendinglist)
        print("Ascending Result: ",ascendinglist)
        menu(list_main)
    elif cho == 'b':
        print("Descending Merge Sort: ")
        mergeSortdown(descendinglist)
        print("Descending Result: ",descendinglist)
        menu(list_main)
    elif cho == 'c':
        print("End of Program")
        exit()

list_main = []
menu(list_main)
