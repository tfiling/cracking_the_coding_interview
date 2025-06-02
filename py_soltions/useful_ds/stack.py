class Stack:
    def __init__(self):
        self.items = []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        if not self.is_empty():
            return self.items.pop()
        raise IndexError("pop from an empty stack")

    def peek(self):
        if not self.is_empty():
            return self.items[-1]
        raise IndexError("peek from an empty stack")

    def is_empty(self):
        return len(self.items) == 0

    def size(self):
        return len(self.items)

    def __len__(self):
        return self.size()

    def __bool__(self):
        return bool(self.items)

    def __str__(self):
        return str(self.items)

    def __iter__(self):
        """Iterate over the stack from top to bottom."""
        return reversed(self.items)
