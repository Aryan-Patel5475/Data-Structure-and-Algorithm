class ListQueues:

    def __init__(self):
        self.items = []
        self.front = self.rear = 0
        self.size = 3

    def enqueue(self, data):

        if self.size == self.rear:
            print('Queue is full')
        else:
            self.items.append(data)
            self.rear += 1

    def dequeue(self):

        if self.front == self.rear:
            print('Queue is empty')
        else:
            data = self.items.pop(0)
            self.rear -= 1
            return data

q = ListQueues()

q.enqueue(10)
q.enqueue(20)
q.enqueue(30)
q.enqueue(40)
print(q.items)
data = q.dequeue()
print(data)
print(q.items)
