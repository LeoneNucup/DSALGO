class Node:
    def __init__(self,data):
        self.left = None
        self.right = None
        self.node = data

def Preorder(root):
    if root:
        print(root.node, end = " ")
        Preorder(root.left)
        Preorder(root.right)

def Inorder(root):
    if root:
        Inorder(root.left)
        print(root.node, end = " ")
        Inorder(root.right)


def Postorder(root):
    if root:
        Postorder(root.left)
        Postorder(root.right)
        print(root.node, end = " ")


def Level(root, height):
    if root is None:
        return
    if height == 1:
        print(root.node ,end=" ")

    Level(root.left , height-1)
    Level(root.right , height-1)

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
    print("[4]Level Order")
    print("[5]Exit")
    cho = input("Input Choice: ")
    while cho not in ['1','2','3','4','5']:
        print("Invalid Input")
        cho = input("Input Choice: ")
    option(cho)


def option(cho):
    if cho == "1":
        print("\nPre Order: " , end =" " )
        Preorder(root)
        menu()
    elif cho == '2':
        print("\nIn Order: " , end =" " )
        Inorder(root)

        menu()

    elif cho == '3':
        print("\nPost Order: " , end =" " )
        Postorder(root)

        menu()

    elif cho == '4':
        print("\nLevel Order: " , end =" " )
        height = 1
        while height < 7:
            Level(root,height)
            height +=1

        menu()

    elif cho == '5':
        exit()

menu()
