class Node:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right


class BinaryTree:

    def __init__(self):
        self.root = None
        self.counter = 0

    def __iter__(self):
        self.to_print = []
        self.to_print.append(self.root)
        return self

    def __next__(self):
        if self.to_print:
            temp = self.to_print.pop(0)
            if temp.left is not None:
                self.to_print.append(temp.left)
            if temp.right is not None:
                self.to_print.append(temp.right)
            return temp.value
        else:
            raise StopIteration

    def push(self, item):
        self.root = self.__push(self.root, item)
        self.counter += 1

    def __push(self, node, item):
        if node is None:
            return Node(item)

        if item < node.value:
            node.left = self.__push(node.left, item)
        else:
            node.right = self.__push(node.right, item)
        return node

    def size(self):
        return self.counter

    def print_values(self):
        return self.__print(self.root)

    def __print(self, node):
        if node is None:
            return
        print(node.value, end=' ')
        self.__print(node.left)
        self.__print(node.right)

    def print_breadth(self):
        to_print = list()
        to_print.append(self.root)
        while to_print:
            temp = to_print.pop(0)
            if temp.left is not None:
                to_print.append(temp.left)
            if temp.right is not None:
                to_print.append(temp.right)
            print(temp.value)

    def contains(self, item):
        temp = self.root
        while temp:
            if temp.value == item:
                return True
            if item > temp.value:
                temp = temp.right
            else:
                temp = temp.left
            if temp is None:
                return False


tree = BinaryTree()
tree.push(5)
tree.push(7)
tree.push(3)
tree.push(1)
tree.push(10)
print(tree.size())
tree.print_values()
print()
print(tree.contains(3))
tree.print_breadth()
print('try BST iter method')
for i, val in enumerate(tree):
    if i == 2:
        break
    print(f'element number: {i}, his value is: {val}')
