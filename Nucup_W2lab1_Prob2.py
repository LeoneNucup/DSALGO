def numbers():
    num = []
    print("Leone Nucup")
    print("Input 10 numbers:")
    x = 1
    for i in range(10):
        num.append(int(input("Item {0} : ".format(x))))
        x += 1
    return num

num = numbers()
def operations(num):
    n = 0
    for i in num:
        n += int(i)
    print("Sum of all Numbers in the list : " , n)
    e_ctr = 0
    e = 0
    for i in num:
        if i % 2 == 0:
            e_ctr +=1
            e += i
    print("Count of all Even Numbers : " , e_ctr)
    print("Sum of all Even Numbers : " , e)
    o_ctr=0
    o = 0
    for i in num:
        if i % 2 != 0:
            o_ctr +=1
            o += i
    print("Count of all Odd Numbers : " , o_ctr)
    print("Sum of all Odd Numbers : " , o)
    l_ctr = 0
    h_ctr = 0
    for i in num:
        if i < 10:
            l_ctr += 1
        elif i >= 10:
            h_ctr += 1
    print("Count of all Numbers Less than 10: ", l_ctr)
    print("Count of all Numbers Greater than or Equal to 10: ", h_ctr)

    num.reverse()
    print("Reverse Order of the List : ", num)
    num.sort()
    print("Ascending order : ", num)

    dup = {i:num.count(i) for i in num}
    print("What number/s occur more than once? {0} Count: {1}".format(max(dup, key=dup.get), max(dup.values())))

    new_val = int(input("Change all Odd values to new value: "))
    for i in num:
        if i % 2 != 0:
            odd = num.index(i)
            num[odd] = new_val
    print(num)

    val = int(input("Input a Value to add in all items greater than 10: "))
    for i in num:
        if i > 10:
            great = num.index(i)
            num[great] += val
    print(num)

operations(num)
