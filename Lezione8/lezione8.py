#1
class Queue:
    pass

class MyStack:
    def __init__(self) -> None:
        self.stack = []

    def push(self, x: int):
        self.stack.append(x)
    
    def top(self):
        element = self.stack[-1]
        return element
    
    def pop(self):
        element = self.stack.pop(-1)
        return element
    
    def empty(self):
        return len(self.stack) == 0

#2
def is_valid_parenthesis(s: str) -> bool:
    
    queue: list =[]
    for read in s:
        queue.append(read)
    ptr: int = 0
    cso: int = 0
    csc: int = 0
    cco: int = 0
    ccc: int = 0

    while (ptr < len(queue)):
        if queue[ptr] == '(':
            ptr += 1
        elif queue[ptr] == '[':
            ptr += 1
            cso += 1
        elif queue[ptr] == '{':
            ptr += 1
            cco += 1
        elif (queue[ptr] == ')') and (queue[ptr - 1] == '('):
            ptr += 1
        elif (queue[ptr] == ']') and (queue[ptr - 1] == '[') or (cso > csc):
            ptr += 1
            csc += 1
        elif (queue[ptr] == '}') and (queue[ptr - 1] == '{') or (cco > ccc):
            ptr += 1
            ccc += 1
        else:
            return False
        
        if (ptr == len(queue)):
            return True   
    if (ptr == len(queue)):
            return True

#3

