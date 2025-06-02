import itertools

from py_soltions.useful_ds.linked_list import LinkedList

def sum_lists(ll1: LinkedList, ll2: LinkedList) -> LinkedList:
    res = LinkedList()
    carry = False
    for digit1, digit2 in itertools.zip_longest(ll1, ll2, fillvalue=0):
        res_curr_digit = digit1 + digit2 + int(carry)
        if res_curr_digit >= 10:
            carry = True
            res_curr_digit -= 10
        else:
            carry = False
        res.insert_at_end(res_curr_digit)
    if carry:
        res.insert_at_end(1)
    return res
