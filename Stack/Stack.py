from Node import Node

class Stack:

    def __init__(self):
        self.top = None
        self.size = 0

    def push(self, data):

        node = Node(data)

        if self.top is None:
            self.top = node
        else:
            node.next = self.top
            self.top = node

        self.size += 1

    def pop(self):

        if self.top is None:
            print('Stack is empty')
        else:
            if self.top.next:
                current = self.top
                next_node = current.next
                current.next = None
                current.data = None
                self.top = next_node
            else:
                current = self.top
                current.next = None
                current.data = None
                self.top = None

        self.size -= 1

    def peek(self):

        if self.top is None:
            return 'empty'
        else:
            return self.top.data

    def print_list(self):

        current = self.top

        while current is not None:
            print(current.data)
            current = current.next



if __name__ == '__main__':
    words = Stack()

    words.push('egg')
    words.push('ham')
    words.push('spam')

    words.peek()
    words.pop()
    words.peek()
    words.pop()
    words.peek()
    words.pop()
    words.peek()