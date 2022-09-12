# Leone Nucup
# Regine Keele
numbers = []
numbers2 = []
file = "c:\W2.txt"

def input_values():
    print("Generate 15 Numbers between 10 and 30 : ")
    i = 1
    while i < 16:
        num = int(input("Value {0} : ".format(i)))
        if num > 10 and num < 30:
            numbers.append(num)
            i+=1
        else:
            print("Invalid Input, Please enter value between 10 and 30")
        if i == 16:
            return numbers

def file_handling(numbers):
    text = open(file, "w")
    text.write("Leone Nucup  \n\n")
    text.write("Regine Keele  \n\n")
    text.write("CS-201 \n\n")
    text.write("Numbers Less than 20 : \n\n")
    for i in numbers:
        if i < 20:
            text.write(str(i)+" ")
    text.write("\n\nNumber of elements Greater than 20 : \n\n")
    count = 0
    for i in numbers:
        if i > 20:
            count+=1
    text.write(str(count))

    text.write("\n\nFirst and Last four digits of the list :\n\n")
    for i in numbers:
        if (numbers.index(i) < 4 or numbers.index(i) > 10) and i not in numbers2:
            text.write(str(i)+" ")
            numbers2.append(i)

    text.write("\n\nSorted List : \n\n")
    numbers2.sort()
    for i in numbers2:
        text.write(str(i)+" ")

    text.close()


numbers = input_values()
file_handling(numbers)
