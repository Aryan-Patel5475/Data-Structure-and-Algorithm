from Stack import Stack

def check(eq):
    bracket = Stack()

    for x in eq:
        if x == '[' or x == '{' or x == '(':
            bracket.push(x)
        elif x == ']':
            last = bracket.peek()
            if last != '[':
                print('Brackets are not balanced')
                return
            else:
                bracket.pop()
        elif x == '}':
            last = bracket.peek()
            if last != '{':
                print('Brackets are not balanced')
                return
            else:
                bracket.pop()
        elif x == ')':
            last = bracket.peek()
            if last != '(':
                print('Brackets are not balanced')
                return
            else:
                bracket.pop()

    if bracket.peek() != 'empty':
        print('Bracket are not balanced')
    else:
        print('Brackets are balanced')


eq = []

sentence = '{(foo)(bar)}[hello](((this)is)a)test'

for x in sentence:
    eq.append(x)

check(eq)