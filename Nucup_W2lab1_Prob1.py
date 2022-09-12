def b_loop():

    for i in range (10):
        myListB.append(int(input("Enter Object: ")))
        if i == 9:
            return myListB

myListA = [2,5,8,1,4,7,3,6,9,1]
myListB = []
myListC = []
myListD = []
myListE = []

myListB = b_loop()

for i in range(5):
    myListC.append(myListA[i])
for i in range(5):
    myListC.append(myListB[i])

myListC.sort()

for i in myListA:
    if i % 2 != 0:
        myListD.append(i)

for i in myListB:
    if i % 2 == 0:
        myListE.append(i)

myListD.extend([1,2,3,4,5])
myListE.extend([6,7,8,9,10])

print(myListA)
print(myListB)
print(myListC)
print(myListD)
print(myListE)

