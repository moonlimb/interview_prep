"""
Stack = collection; abstract data type (ADT)
    - a LIFO ("last in, first out") data structure; last item added is the first to be removed.

ADT is defined by the operations that can be performed on it. 
Interface = set of operations that define an ADT

"""

class Stack():
    
    "initialize an empty stack"
    def __init__(self):
        self.items = []

    "append an item to the stack"
    def push(self, item):
        self.items.append(item)

    "remove an item from the stack"
    def pop(self):
        self.items.pop()

    "returns a top element in the stack; does not modify the stack"
    def peek(self):
        return self.items[-1] 

    "returns true if stack is empty"
    def is_empty(self):
        return (self.items == [])

    "returns the number of items in the stack"
    def size(self):
        return len(self.items)

    "returns a Stack represenation, listening one item per line from top to bottom"
    def __repr__(self):
        if self.items == []:
            return 'Stack()'
        top_to_bottom = self.items[::-1] 
        return "Stack:\nTop: %s \nBottom" %('\n'.join([str(item) for item in top_to_bottom]))

    "returns all the items in a Stack as a str"
    def __str__(self):
        return str(self.items)
