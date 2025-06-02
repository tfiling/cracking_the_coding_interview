import pytest
from stack import Stack

def test_stack_is_empty_initially():
    stack = Stack()
    # A new stack should be empty
    assert stack.is_empty() is True
    assert len(stack) == 0
    assert not stack

def test_push_increases_size():
    stack = Stack()
    stack.push(1)
    stack.push(2)
    # After pushing two elements, size should be 2
    assert stack.size() == 2
    assert len(stack) == 2

def test_pop_returns_last_element():
    stack = Stack()
    stack.push("a")
    stack.push("b")
    popped = stack.pop()
    # Should return the most recently pushed element
    assert popped == "b"
    # Size should decrease by one
    assert stack.size() == 1

def test_pop_on_empty_stack_raises_error():
    stack = Stack()
    with pytest.raises(IndexError, match="pop from an empty stack"):
        stack.pop()

def test_peek_returns_top_element_without_removing():
    stack = Stack()
    stack.push(10)
    stack.push(20)
    top = stack.peek()
    # Top element should be 20
    assert top == 20
    # Ensure the element is not removed
    assert stack.size() == 2

def test_peek_on_empty_stack_raises_error():
    stack = Stack()
    with pytest.raises(IndexError, match="peek from an empty stack"):
        stack.peek()

def test_bool_evaluation():
    stack = Stack()
    # An empty stack should evaluate to False
    assert not stack
    stack.push(100)
    # A non-empty stack should evaluate to True
    assert stack

def test_str_representation():
    stack = Stack()
    # Initially, the string representation should be an empty list
    assert str(stack) == "[]"
    stack.push(1)
    stack.push(2)
    # Since __str__ returns str(self.items) and items are appended,
    # the expected string is "[1, 2]"
    assert str(stack) == "[1, 2]"

def test_iterator_returns_elements_from_top_to_bottom():
    stack = Stack()
    stack.push('first')
    stack.push('second')
    stack.push('third')
    # The iterator should yield elements from top to bottom (i.e. last pushed first)
    items = list(stack)
    assert items == ['third', 'second', 'first']
