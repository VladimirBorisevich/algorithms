class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


class Queue:
    def __init__(self):
        self.head = None
        self.tail = None
        self.counter = 0

    def is_empty(self):
        return self.counter == 0

    def push(self, item):
        if self.is_empty():
            self.head = Node(item)
            self.tail = self.head
            self.counter += 1
            return

        self.tail.next = Node(item)
        self.tail = self.tail.next
        self.counter += 1

    def pop(self):
        temp = self.head
        self.head = temp.next
        self.counter -= 1
        return temp.value

    def print_values(self):
        temp = self.head
        while temp is not None:
            print(temp.value, end=' ')
            temp = temp.next

    def size(self):
        return self.counter


q = Queue()
q.push(5)
q.push(2)
q.push(10)
print(q.size())
q.print_values()
