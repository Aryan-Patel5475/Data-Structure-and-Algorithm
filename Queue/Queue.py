from Node import Node

class Queue:

    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0

    def enqueue(self, data):

        node = Node(data)

        if self.head == None:
            self.head = node
            self.tail = node
        else:
            current = self.tail
            current.next = node
            node.prev = current
            self.tail = node

        self.size += 1

    def dequeue(self):

        if self.head is None:
            print('Queue is empty')
            return

        if self.head == self.tail:
            current = self.head
            current.prev = None
            current.next = None
            current.data = None
            self.head = None
            self.tail = None
        else:
            current = self.tail
            prev_node = current.prev
            prev_node.next = None
            current.prev = None
            self.tail = prev_node
            current.next = None
            current.data = None

        self.size -= 1

    def print_list(self):

        if self.head is None:
            print('List is empty')
            return

        current = self.head

        while current is not None:
            print(current.data)
            current = current.next

q = Queue()

q.enqueue(10)
q.enqueue(20)
q.enqueue(30)
q.print_list()
print()

#30
q.dequeue()
q.print_list()
print()

#20
q.dequeue()
q.print_list()
print()

#10
q.dequeue()
q.print_list()