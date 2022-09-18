class Node:
    def __init__(self, data):
        self.left = None
        self.right = None
        self.data = data
    def treeprint(self):
            if self.left:
                self.left.treeprint()
            print(self.data, end = " ")
            if self.right:
                self.right.treeprint()

root = Node(8)

root.left = Node(4)

root.left.left = Node(2)
root.left.left.left = Node(1)
root.left.left.right = Node(3)

root.left.right = Node(6)
root.left.right.left = Node(5)
root.left.right.right = Node(7)

root.right = Node(12)

root.right.left = Node(10)
root.right.left.left = Node(9)
root.right.left.right = Node(11)

root.right.right = Node(14)
root.right.right.left = Node(13)
root.right.right.right = Node(15)

root.treeprint()
