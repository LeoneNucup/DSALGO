class Node:

    def __init__(self,data=None):
        self.data = data
        self.next = None

class colors:

    def __init__(self):
        self.head=None

    def listprint(self):

        printval = self.head
        print("\n")
        while printval is not None:
            print(printval.data, end = " ")
            printval=printval.next


    def beginning(self, newdata):

        newnode = Node(newdata)
        newnode.next = self.head.next
        self.head.next = newnode


    def last(self,newdata):
        newnode = Node(newdata)
        lastnode = self.head
        if lastnode == None:
            self.head = newnode
            return
        while(lastnode.next):
            lastnode = lastnode.next
        lastnode.next = newnode

    def middle(self,middle_node,newdata):
        if middle_node == None:
            print("No Node")
            return
        newnode = Node(newdata)
        newnode.next = middle_node.next
        middle_node.next = newnode

    def remove(self,remove):
        Head = self.head
        if Head is not None and Head.data == remove:
            self.head = Head.next
            Head = None
            return
        while Head is not None:
            if Head.data == remove:
                break
            prev = Head
            Head = Head.next
        if Head == None:
            print("\nError: Input not in List")
            return
        prev.next = Head.next
        Head = None

colors = colors()

colors.head = Node("Colors")
A1 = Node("Red")
A2 = Node("Brown")
A3 = Node("Orange")
A4 = Node("White")
A5 = Node("Green")
A6 = Node("Yellow")
A7 = Node("Purple")
A8 = Node("Blue")
A9 = Node("Pink")
A10 = Node("Black")


colors.head.next = A1
A1.next = A2
A2.next = A3
A3.next = A4
A4.next = A5
A5.next = A6
A6.next = A7
A7.next = A8
A8.next = A9
A9.next = A10

def menu():
        print("""\n\nOptions :
        \n[1] Insert at the beginning
        \n[2] Insert at the end
        \n[3] Insert In between
        \n[4] Delete
        \n[5] Display List
        \n[6] Exit\n""")
        cho = int(input("Input Choice: "))
        option(cho)


def option(cho):
        if cho == 1:
            newdata=input("Input New Color: ")
            colors.beginning(newdata)
            colors.listprint()
            menu()
        elif cho == 2:
            newdata=input("Input New Color at End: ")
            colors.last(newdata)
            colors.listprint()
            menu()

        elif cho == 3:
            newdata = input("Input New Color In Between: ")
            colors.middle(A6.next,newdata)
            colors.listprint()
            menu()

        elif cho == 4:
            remove = input("Input Color to Delete : ")
            colors.remove(remove)
            colors.listprint()
            menu()

        elif cho == 5:
            colors.listprint()
            menu()

        elif cho == 6:
            exit()


menu()
