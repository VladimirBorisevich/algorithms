
class Node:
    def __init__(self,value):
        self.value = value

class Binary_tree:

    def __init__(self):
        self.head = None
        self.left = None
        self.right = None

    def push(self, item):

        if self.head == None:
            self.head = Node(item)
            return

        if item < self.head
            self.left = Node(item)

    def print_value(self):
        pass

    def rebuild_tree(self):
        pass