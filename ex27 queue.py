class Fila:
    def __init__(self):
        # Initialize an empty list to store the queue elements.
        self.elementos = []
    
    def enqueue(self, item):
        # Add a new item to the end (rear) of the queue.
        # We use .append() because it efficiently adds elements to the end of the list.
        self.elementos.append(item)
    
    def dequeue(self):
        # Remove and return the item from the front (head) of the queue.
        # We check if it's empty first to avoid errors.
        # We use .pop(0) to remove the element at index 0 (the first one added).
        if not self.esta_vazia():
            return self.elementos.pop(0)
        return None
    
    def esta_vazia(self):
        # Return True if the length of the list is 0, meaning the queue is empty.
        return len(self.elementos) == 0
    
    def tamanho(self):
        # Return the current number of items in the queue.
        return len(self.elementos)

# --- Using the queue ---
f = Fila()
f.enqueue("Cliente A") # List: ["Cliente A"]
f.enqueue("Cliente B") # List: ["Cliente A", "Cliente B"]
f.enqueue("Cliente C") # List: ["Cliente A", "Cliente B", "Cliente C"]

# 1. dequeue() removes the first item added ("Cliente A") and prints it.
print(f.dequeue()) # Output: "Cliente A"
# List is now: ["Cliente B", "Cliente C"]

# 2. dequeue() removes the next item in line ("Cliente B") and prints it.
print(f.dequeue()) # Output: "Cliente B"