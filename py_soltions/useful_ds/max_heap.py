import heapq
import typing

class MaxHeap:
    """Max heap wrapper around heapq, that supports only min heap"""
    _min_heap = []

    def __init__(self, elements: typing.List[int]):
        self._min_heap = [-1 * num for num in elements]
        heapq.heapify(self._min_heap)

    def peek_max(self) -> int:
        return -1 * self._min_heap[0]

    def pop_max(self) -> int:
        res = -1 * self._min_heap.pop(0)
        heapq.heapify(self._min_heap)
        return res

    def push(self, element: int):
        heapq.heappush(self._min_heap, -1 * element)
