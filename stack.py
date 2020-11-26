#
class Node:

    def __init__(self, value, next):
        self.value = value
        self.next = next


class Stack:

    def __init__(self):
        self.head = None
        self.counter = 0

    def is_empty(self):
        return self.counter == 0

    def push(self, item):
        self.head = Node(item, self.head)
        self.counter += 1

    def print_values(self):
        temp = self.head
        while temp is not None:
            print(temp.value, end=' ')
            temp = temp.next
        print('\n')

    def pop(self):
        temp = self.head
        self.head = temp.next
        self.counter -= 1
        return temp.value

    def size(self):
        return self.counter


stack = Stack()

stack.push(1)
stack.push(2)
stack.push(30)
stack.print_values()
print('size = ', stack.size())

stack.pop()
stack.pop()
stack.pop()

stack.push(10)
stack.pop()
print('size = ', stack.size())
