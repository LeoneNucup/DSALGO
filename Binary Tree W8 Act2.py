class Node:
    def __init__(self,data):
        self.left = None
        self.right = None
        self.data = data

def preorder(root):
    if root:
        print(root.data, end = " ")
        preorder(root.left)
        preorder(root.right)

def inorder(root):
    if root:
        inorder(root.left)
        print(root.data, end = " ")
        inorder(root.right)


def postorder(root):
    if root:
        postorder(root.left)
        postorder(root.right)
        print(root.data, end = " ")


def level(root, height):
    if root is None:
        return
    if height == 1:
        print(root.data ,end=" ")

    level(root.left , height-1)
    level(root.right , height-1)

root = Node (35)

root.left = Node(10)

root.left.left = Node(8)
root.left.left.left = Node(6)
root.left.left.right = Node(9)

root.left.right = Node(18)
root.left.right.left = Node(15)
root.left.right.right = Node(28)

root.right = Node(75)

root.right.left = Node(40)
root.right.left.left = Node(38)
root.right.left.right = Node(45)
root.right.left.right.left = Node(43)

root.right.left.right.right = Node(50)
root.right.left.right.right.left = Node(46)
root.right.left.right.right.right = Node(55)

root.right.right = Node(80)



def menu():
    print("\n\n[1]Pre Order")
    print("[2]In Order")
    print("[3]Post Order")
    print("[4]level Order")
    print("[5]Exit")
    cho = input("Input Choice: ")
    while cho not in ['1','2','3','4','5']:
        print("Invalid Input")
        cho = input("Input Choice: ")
    option(cho)


def option(cho):
    if cho == "1":
        print("\nPre Order: " , end =" " )
        preorder(root)
        menu()
    elif cho == '2':
        print("\nIn Order: " , end =" " )
        inorder(root)

        menu()

    elif cho == '3':
        print("\nPost Order: " , end =" " )
        postorder(root)

        menu()

    elif cho == '4':
        print("\nlevel Order: " , end =" " )
        height = 1
        while height < 7:
            level(root,height)
            height +=1

        menu()

    elif cho == '5':
        exit()

menu()
