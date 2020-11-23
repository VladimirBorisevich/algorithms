#
class Node:

    def __init__(self, value):
        self.value = value
        self.next = None


class Stack:

    def __init__(self):
        self.value = None
        self.head = None
        self.temp = None
        self.counter = 0

    def isEmpty(self):

        if self.counter == 0:
            print('stack is empty')
            return True
        else:
            print('stack is not empty')
            return False

    def push(self, item):

        if self.counter == 0:
            self.head = Node(item)
            self.counter += 1
            return

        if self.counter == 1:
            self.value = Node(item)
            self.head.next = self.value
            self.counter += 1
            return

        self.value.next = Node(item)
        self.counter += 1

    def print_values(self):
        self.temp = self.head
        while self.temp:
            print(self.temp.value, end=' ')
            self.temp = self.temp.next
        print('')

    def pop(self):

        if self.counter == 0:
            return print('stack is empty')

        if self.counter == 1:
            print(self.head.value)
            self.head = None
            self.value = None
            self.counter = 0
            return

        print(self.value.next.value)
        self.value.next = self.value
        self.counter -= 1

    def size(self):
        print('size of stack is ', self.counter)


stack = Stack()

stack.push(1)
stack.push(2)
stack.push(30)
stack.print_values()
stack.size()

stack.pop()
stack.pop()
stack.pop()
stack.pop()

stack.push(10)
stack.pop()
stack.pop()
stack.size()


