from Node import Node

class Single_linked_list:

    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0

    def append(self, data):
        self.size += 1
        node = Node(data)
        if self.tail is not None:
            self.tail.next = node
            self.tail = node
        else:
            self.head = node
            self.tail = node

    def append_at_location(self, index, data):

        if index == 1:
            node = Node(data)
            node.next = self.head
            self.head = node
            self.size += 1
        elif index == self.size + 1:
            self.append(data)
        elif index > self.size:
            print('The list has less number of elements')
            return
        else:
            node = Node(data)
            current = self.head
            prev_node = self.head
            count = 1

            while count < index:
                prev_node = current
                current = current.next
                count += 1

            prev_node.next = node
            node.next = current
            self.size += 1

    def search(self, data):

        if self.head is None:
            print('List is empty')
            return

        current = self.head
        count = 1
        while current is not None:
            if current.data == data:
                print('Found at:', count, end=' ')
                return True
            current = current.next
            count += 1
        return False

    def delete_head(self):
        if self.head is None:
            print('List is empty')
            return

        current = self.head
        next_node = current.next
        self.head = next_node
        current.next = None
        current.data = None
        self.size -= 1

        if self.size == 1:
            self.tail = next_node

    def delete_tail(self):

        if self.size == 1:
            self.delete_head()
            return

        current = self.head
        prev_node = self.head

        while current.next is not None:
            prev_node = current
            current = current.next

        current.next = None
        current.data = None
        prev_node.next = None
        self.tail = prev_node
        self.size -= 1

    def delete_at_location(self, index):

        if index == 1:
            self.delete_head()
        elif index == self.size:
            self.delete_tail()
        else:
            current = self.head
            prev_node = self.head
            next_node = current.next
            count = 1

            while current is not None:
                prev_node = current
                current = current.next
                next_node = next_node.next
                count += 1
                if count == index:
                    break

            prev_node.next = next_node
            current.data = None
            current.next = None
            self.size -= 1

    def clear(self):
        current = self.head

        while current is not None:
            next_node = current.next
            current.next = None
            current.data = None
            current = next_node

        self.head = None
        self.tail = None

    def print_list(self):
        current = self.head

        while current is not None:
            print(current.data)
            current = current.next

def main():
    words = Single_linked_list()

    words.append('egg')
    words.append('ham')
    words.append('spam')
    words.print_list()
    print('Size:', words.size)
    print()

    print('Append at Location:')
    words.append_at_location(1, 'bread')
    words.print_list()
    print('Size:', words.size)
    print()

    words.append_at_location(2, 'cheese')
    words.append_at_location(6, 'bread')
    words.print_list()
    print('Size:', words.size)
    print()

    print('Delete head and tail:')
    words.delete_head()
    words.delete_tail()
    words.print_list()
    print('Size:', words.size)
    print()

    print('Delete at Location:')
    words.delete_at_location(3)
    words.print_list()
    print('Size:', words.size)
    print()

    print('Search:')
    print(words.search('ham'))
    print(words.search('spam'))
    print()

    print('Clear:')
    words.clear()
    words.print_list()

main()