#INFIX TO POSTFIX
from collections import deque
def infix_to_postfix(expression):
    output = []
    stack=deque()

    for token in expression:
        if token.isnumeric():
            output.append(token)
        elif token=='(':
            stack.append(token)
        elif token==')':
            while stack and stack [-1]!='(':
                output.append(stack.pop())