mylist=[5,9,7,3,1,0,4,6,8,2]

mytuples=(5,2,7,1,3,6,9,8,2,8)

mysets={5,9,1,3,7,2,6,8,4,0}


# 1.
print(mylist[1:8])

# 2.
print(mylist[0:6])

# 3.
print(mylist[-8:-2])

# 4.
mylist[1] = 8

# 5.
i = -5
while i < 0:
    print(mylist[i],end=",")
    i+=1

# 6.
mylist.insert(5,10)

# 7.
mylist.remove(8)
mylist.pop(8)

# 8.
print(len(mytuples))

# 9.
print(mytuples.count(8))

# 10.
mysets.remove(2)

# 11.
mysets.clear()

#12.
mysets.update([5,6,8,9])
#13.
del mytuples
# 14.
for i in mylist:
    if i % 2 != 0:
        print(i,end=",")
print("\n")
# 15.
for i in mylist:
    print(i - 3,end=",")
print("\n")
list1=[2,4,6,8,10]

list2=[4,8,2,6]

tuple1=(1,3,5,7,9)

tuple2=(6,7,8,9,4)

set1={2,4,6,8}

set2={3,6,2,4}
# 16.
x=set1.intersection(set2)
print(x) # {2, 4, 6}
# 17.
list1.sort()
print(list1) # [2, 4, 6, 8, 10]
# 18.
list2.extend(list1)
print(list2) # [4, 8, 2, 6, 2, 4, 6, 8, 10]
# 19.
Y = tuple1 + tuple2
print(Y) # (1, 3, 5, 7, 9, 6, 7, 8, 9, 4)
# 20.
z = set2.difference(set1)
print(z) # {3}
# 21.
set1.update([2,9,3,6])
print(set1)
# 22.
list2.reverse()
print(list2) # [6, 2, 8, 4]
# 23.
x = tuple2.count(4)
print(x) # 1
# 24.
set2.discard(3)
print(set2)
# 25. kung aayusin
list2.pop()
print(list2) # [4, 8, 2]
# 25 kung susundan ung nasa activity exactly
list2.pop
print(list2) # [4, 8, 2, 6]

