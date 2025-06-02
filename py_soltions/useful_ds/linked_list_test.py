import pytest

import linked_list

@pytest.fixture(scope="function")
def empty_list():
    return linked_list.LinkedList()

@pytest.fixture(scope="function")
def populated_list():
    empty_list = linked_list.LinkedList()
    empty_list.insert_at_end(1)
    empty_list.insert_at_end(2)
    empty_list.insert_at_end(3)
    return empty_list

def test_insert_at_beginning(empty_list):
    empty_list.insert_at_beginning(1)
    assert_linked_list_contents(empty_list, [1])

def test_insert_at_beginning_multiple(empty_list):
    empty_list.insert_at_beginning(1)
    empty_list.insert_at_beginning(2)
    empty_list.insert_at_beginning(1)
    assert_linked_list_contents(empty_list, [1, 2, 1])

@pytest.mark.parametrize("index, value, expected", [
    (0, 0, [0, 1, 2, 3]),
    (1, 0, [1, 0, 2, 3]),
    (2, 0, [1, 2, 0, 3]),
])
def test_insert_at_index_populated_list(populated_list, index, value, expected):
    populated_list.insert_at_index(value, index)
    assert populated_list.size() == len(expected)
    assert [data for data in populated_list] == expected


def test_insert_at_index_empty_list(empty_list):
    empty_list.insert_at_index(1, 0)
    assert_linked_list_contents(empty_list, [1])

def test_insert_at_index_raises_index_error(populated_list):
    with pytest.raises(IndexError):
        populated_list.insert_at_index(4, 4)

def test_insert_at_index_raises_value_error(populated_list):
    with pytest.raises(ValueError):
        populated_list.insert_at_index(5, -1)

def test_insert_at_end(empty_list):
    empty_list.insert_at_end(1)
    assert_linked_list_contents(empty_list, [1])
    empty_list.insert_at_end(2)
    assert_linked_list_contents(empty_list, [1, 2])
    empty_list.insert_at_end(3)
    assert_linked_list_contents(empty_list, [1, 2, 3])

@pytest.mark.parametrize("index, expected", [
    (1, [1, 3]),
    (0, [2, 3]),
])
def test_remove_at_index(populated_list, index, expected):
    populated_list.remove_at_index(index)
    assert_linked_list_contents(populated_list, expected)

def test_remove_at_index_empty_list(empty_list):
    with pytest.raises(IndexError):
        empty_list.remove_at_index(0)

def test_remove_at_index_out_of_range(populated_list):
    with pytest.raises(IndexError):
        populated_list.remove_at_index(3)

def test_remove_node(populated_list):
    populated_list.remove_node(2)
    assert_linked_list_contents(populated_list, [1, 3])

def test_remove_non_existent_node(populated_list):
    was_removed = populated_list.remove_node(4)
    assert was_removed == False
    assert_linked_list_contents(populated_list, [1, 2, 3])

def test_size(empty_list, populated_list):
    assert empty_list.size() == 0
    assert populated_list.size() == 3
    populated_list.remove_node(2)
    assert populated_list.size() == 2

def test_empty_list_operations(empty_list):
    with pytest.raises(IndexError):
        empty_list.remove_at_index(0)
    was_removed = empty_list.remove_node(1)  # Should not raise an error
    assert was_removed == False
    assert empty_list.size() == 0
    with pytest.raises(IndexError):
        empty_list.insert_at_index(1, 1)
    empty_list.insert_at_index(1, 0)  # Should work
    assert_linked_list_contents(empty_list, [1])

def test_multiple_operations(empty_list):
    empty_list.insert_at_beginning(1)
    empty_list.insert_at_end(3)
    empty_list.insert_at_index(2, 1)
    assert_linked_list_contents(empty_list, [1, 2, 3])
    empty_list.remove_at_index(1)
    assert_linked_list_contents(empty_list, [1, 3])
    empty_list.insert_at_beginning(0)
    empty_list.insert_at_end(4)
    assert_linked_list_contents(empty_list, [0, 1, 3, 4])

def assert_linked_list_contents(actual: linked_list.LinkedList, expected: list):
    assert actual.size() == len(expected)
    assert [data for data in actual] == expected

def test_empty_lists_are_equal():
    ll1 = linked_list.LinkedList()
    ll2 = linked_list.LinkedList()
    assert ll1 == ll2, "Two empty lists should be equal."

def test_lists_with_same_elements_are_equal():
    data = [1, 2, 3, 4, 5]
    ll1 = linked_list.from_list(data)
    ll2 = linked_list.from_list(data)
    assert ll1 == ll2, "Lists built from the same data should be equal."

def test_lists_with_different_lengths_are_not_equal():
    ll1 = linked_list.from_list([1, 2, 3])
    ll2 = linked_list.from_list([1, 2, 3, 4])
    # Even if the shorter list's elements match the beginning of the longer list,
    # they should not be considered equal because the lengths differ.
    assert ll1 != ll2, "Lists of different lengths should not be equal."

def test_lists_with_different_elements_are_not_equal():
    ll1 = linked_list.from_list([1, 2, 3])
    ll2 = linked_list.from_list([1, 2, 4])
    assert ll1 != ll2, "Lists with different elements should not be equal."

def test_lists_with_same_elements_different_order_are_not_equal():
    ll1 = linked_list.from_list([1, 2, 3])
    ll2 = linked_list.from_list([3, 2, 1])
    assert ll1 != ll2, "Order of elements matters, so lists with same elements in different order should not be equal."
