from Node import Node

class DoublyLinkedList:

    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0

    def append_tail(self, data):

        node = Node(data)

        if self.tail is not None:
            current = self.tail
            current.next = node
            node.prev = current
            self.tail = node
        else:
            self.head = node
            self.tail = node

        self.size += 1

    def append_head(self, data):

        node = Node(data)

        if self.tail is not None:
            current = self.head
            current.prev = node
            node.next = current
            self.head = node
        else:
            self.head = node
            self.tail = node

        self.size += 1

    def append_at_location(self, index, data):

        if index > (self.size + 1):
            print('List is not big enough')
            return

        if index == 1:
            self.append_head(data)
            return
        elif index == self.size + 1:
            self.append_tail(data)
            return

        node = Node(data)
        current = self.head
        prev_node = self.head
        count = 1

        while count != index:
            prev_node = current
            current = current.next
            count += 1

        prev_node.next = node
        node.prev = prev_node
        current.prev = node
        node.next = current
        self.size += 1

    def search(self, data):

        current = self.head
        count = 1

        while current is not None:
            if current.data == data:
                print('data is at index:', count)
                return
            count += 1
            current =  current.next

        print('Data not found')

    def delete_head(self):

        if self.tail is None:
            print('List is empty')
            return

        current = self.head
        next_node = current.next
        current.next = None
        current.data = None
        next_node.prev = current.prev
        self.head = next_node
        self.size -= 1

    def delete_tail(self):

        if self.tail is None:
            print('List is empty')
            return

        current = self.tail
        prev_node = current.prev
        current.prev = None
        current.data = None
        prev_node.next = current.next
        self.tail = prev_node
        self.size -= 1

    def delete_at_location(self, index):

        if index > self.size:
            print('List is not that big')
            return
        elif index == 1:
            self.delete_head()
            return
        elif index == self.size:
            self.delete_tail()
            return

        prev_node = self.head
        current = prev_node.next
        next_node = current.next
        count = 2

        while count != index:
            prev_node = prev_node.next
            current = current.next
            next_node = next_node.next
            count += 1

        prev_node.next = next_node
        next_node.prev = prev_node
        current.next = None
        current.prev = None
        current.data = None
        self.size -= 1

    def delete_data(self, data):

        if self.head.data == data:
            self.delete_head()
            return
        elif self.tail.data == data:
            self.delete_tail()
            return

        found = False
        prev_node = self.head
        current = prev_node.next
        next_node = current.next
        count = 2

        while current is not None and count < self.size:

            if current.data == data:
                found = True
                break

            prev_node = prev_node.next
            current = current.next
            next_node = current.next
            count += 1

        if found is True:
            prev_node.next = next_node
            next_node.prev = prev_node
            current.next = None
            current.prev = None
            current.data = None
            self.size -= 1
        else:
            print('Data not found')

    def clear(self):

        current = self.head

        while current is not None:
            node = current
            current = current.next
            node.prev = None
            node.next = None
            node.data = None

        self.head = None
        self.tail = None

    def print_list(self):

        current = self.head

        while current is not None:
            print(current.data)
            current = current.next

def main():

    words = DoublyLinkedList()

    print('Appending at the tail:')
    words.append_tail('egg')
    words.append_tail('ham')
    words.append_tail('spam')
    words.print_list()
    print('Size:', words.size)
    print()

    print('Appending at the head:')
    words.append_head('bread')
    words.print_list()
    print('Size:', words.size)
    print()

    print('Appending at index:')
    words.append_at_location(2, 'cheese')
    words.append_at_location(6, 'bread')
    words.print_list()
    print('Size:', words.size)
    print()

    print('Search:')
    words.search('spam')
    words.search('bacon')
    print()

    print('Delete head:')
    words.delete_head()
    words.print_list()
    print('Size:', words.size)
    print()

    print('Delete tail:')
    words.delete_tail()
    words.print_list()
    print('Size:', words.size)
    print()

    print('Delete at index:')
    words.delete_at_location(3)
    words.print_list()
    print('Size:', words.size)
    print()

    print('Delete data:')
    words.delete_data('egg')
    words.delete_data('bread')
    words.print_list()
    print('Size:', words.size)
    print()

main()