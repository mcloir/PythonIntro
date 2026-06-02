class Stack:
    def __init__(self):
        # Initialize an empty list to store stack items
        self.items = []

    def push(self, item):
        # Add an item to the top of the stack (the end of the list)
        self.items.append(item) 
    
    def pop(self):
        # Remove and return the top item if the stack is not empty
        if not self.is_empty():
            return self.items.pop()
        return None
    
    def peek(self):
        # Return the top item without removing it (using index -1)
        if not self.is_empty():
            return self.items[-1]
        return None

    def is_empty(self):
        # Return True if the list is empty, otherwise False
        return len(self.items) == 0
    
# Create a new instance of the Stack
p = Stack()
p.push(10)
p.push(20)
p.push(30)

# 1. pop() removes the last element (30) and returns it
print(p.pop())  # Output: 30

# 2. peek() looks at the current top element (20) without removing it
print(p.peek()) # Output: 20