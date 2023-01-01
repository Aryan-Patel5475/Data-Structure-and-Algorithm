size = 3
data = [0]*(size)
top = -1

def push(x):
    global top
    if top >= size - 1:
        print('Stack Overflow')
    else:
        top = top + 1
        data[top] = x

def pop():

    global top
    if top == -1:
        print('Stack Underflow')
    else:
        data[top] = 0
        top = top - 1

def peek():
    global top
    if top == -1:
        print('Stack is empty')
    else:
        print(data[top])

push('egg')
push('ham')
peek()
pop()
peek()
pop()
peek()