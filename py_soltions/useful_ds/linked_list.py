import typing

class _Node:
    def __init__(self, data):
        self.data = data
        self.next: typing.Optional[_Node] = None


class LinkedList:
    def __init__(self):
        self.head: typing.Optional[_Node] = None

    def insert_at_beginning(self, data):
        new_node = _Node(data)
        new_node.next = self.head
        self.head = new_node

    def insert_at_index(self, data, index):
        if index < 0:
            raise ValueError("Index must be non-negative")

        if index == 0:
            self.insert_at_beginning(data)
            return

        new_node = _Node(data)
        current = self.head
        for _ in range(index - 1):
            if current is None:
                raise IndexError("Index out of range")
            current = current.next

        if current is None:
            raise IndexError("Index out of range")

        new_node.next = current.next
        current.next = new_node

    def insert_at_end(self, data):
        new_node = _Node(data)
        if self.head is None:
            self.head = new_node
            return

        current = self.head
        while current.next:
            current = current.next
        current.next = new_node

    def remove_at_index(self, index):
        if self.head is None:
            raise IndexError("Cannot remove from empty list")

        if index < 0:
            raise ValueError("Index must be non-negative")

        if index == 0:
            self.head = self.head.next
            return

        current = self.head
        for _ in range(index - 1):
            if current.next is None:
                raise IndexError("Index out of range")
            current = current.next

        if current.next is None:
            raise IndexError("Index out of range")

        current.next = current.next.next

    def remove_node(self, data) -> bool:
        if self.head is None:
            return False

        if self.head.data == data:
            self.head = self.head.next
            return True

        current = self.head
        while current.next and current.next.data != data:
            current = current.next

        if current.next:
            current.next = current.next.next
            return True
        return False

    def size(self):
        count = 0
        current = self.head
        while current:
            count += 1
            current = current.next
        return count

    def __iter__(self):
        current = self.head
        while current:
            yield current.data
            current = current.next

    def __str__(self):
        return ' -> '.join(str(item) for item in self)

    def __len__(self):
        return self.size()

    def __eq__(self, other: "LinkedList"):
        if len(self) != len(other):
            return False
        for e1, e2 in zip(self, other):
            if e1 != e2:
                return False
        return True


def from_list(lst: list) -> LinkedList:
    res = LinkedList()
    for elem in lst:
        res.insert_at_end(elem)
    return res
