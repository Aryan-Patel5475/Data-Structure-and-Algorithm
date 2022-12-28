from Node import Node

class CircularLinkedList:

    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0

    def append_tail(self, data):
        node = Node(data)

        if self.head is not None:
            current = self.tail
            current.next = node
            node.next = self.head
            self.tail = node
        else:
            self.head = node
            self.tail = node
            node.next = self.head
        self.size += 1

    def append_head(self, data):
        node = Node(data)

        if self.head is not None:
            current = self.head
            node.next = current
            self.tail.next = node
            self.head = node
        else:
            self.head = node
            self.tail = node
            node.next = self.head
        self.size += 1

    def append_at_location(self, index, data):

        if index > self.size + 1:
            print('List is not big enough')
            return
        elif index == 1:
            self.append_head(data)
            return
        elif index == self.size + 1:
            self.append_tail(data)
            return
        else:
            node = Node(data)
            current = self.head
            next_node = current.next
            count = 2

            while count != index:
                current = current.next
                next_node = next_node.next
                count += 1

            current.next = node
            node.next = next_node
            self.size += 1

    def delete_head(self):

        if self.head is None:
            print('List is empty')
            return

        current = self.head
        tail = self.tail
        next_node = current.next
        tail.next = next_node
        current.next = None
        current.data = None
        self.head = next_node
        self.size -=1

    def delete_tail(self):

        if self.head is None:
            print('List is empty')
            return

        current = self.head
        prev_node = self.head
        count = 1

        while count != self.size:
            prev_node = current
            current = current.next
            count += 1

        prev_node.next = self.head
        self.tail = prev_node
        current.next = None
        current.data = None
        self.size -= 1

    def delete_data(self, data):

        if self.head is None:
            print('List is empty')
            return
        elif self.head.data == data:
            self.delete_head()
            return
        elif self.tail.data == data:
            self.delete_tail()
            return
        else:

            current = self.head
            prev_node = self.head
            found = False

            while found is False and prev_node != self.tail:
                if current.data == data:
                    found = True
                    break
                prev_node = current
                current = current.next

            if found is False:
                print('Data not found')
                return

            prev_node.next = current.next
            current.next = None
            current.data = None
            self.size -= 1

    def search(self, data):

        if self.tail.data == data:
            print('Found')
            return

        current = self.head

        while current != self.tail:
            if current.data == data:
                print('Found')
                return
            current = current.next

        print('Not Found')

    def print_list(self):

        current = self.head
        count = 0
        while count < self.size:
            print(current.data)
            current = current.next
            count += 1

def main() :

    words = CircularLinkedList()

    print('Append at tail:')
    words.append_tail('egg')
    words.append_tail('ham')
    words.append_tail('spam')
    words.append_tail('bacon')
    words.print_list()
    print('Size:', words.size)
    print()

    print('Appending at head:')
    words.append_head('bread')
    words.print_list()
    print('Size:', words.size)
    print()

    print('Append at location:')
    words.append_at_location(2, 'cheese')
    words.print_list()
    print('Size:', words.size)
    print()

    print('Delete head:')
    words.delete_head()
    words.print_list()
    print('Size:', words.size)
    print()

    print('Delete the tail:')
    words.delete_tail()
    words.print_list()
    print('Size:', words.size)
    print()

    print('Delete the data:')
    words.delete_data('bread')
    words.delete_data('ham')
    words.print_list()
    print('Size:', words.size)
    print()

    print('Search:')
    words.search('ham')
    words.search('spam')

main()