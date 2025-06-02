# https://neetcode.io/problems/minimum-stack
import heapq


class MinStack:

    def __init__(self):
        self._heapq = []
        self._pending_heap_pop = {}
        self._stack = []

    def push(self, val: int) -> None:
        self._stack.append(val)
        heapq.heappush(self._heapq, val)

    def pop(self) -> None:
        popped_val = self._stack.pop()
        self._pending_heap_pop[popped_val] = self._pending_heap_pop.get(popped_val, 0) + 1

    def top(self) -> int:
        return self._stack[-1]

    def getMin(self) -> int:
        res = self._heapq[0]
        while res in self._pending_heap_pop:
            heapq.heappop(self._heapq)
            if self._pending_heap_pop[res] == 1:
                del self._pending_heap_pop[res]
            else:
                self._pending_heap_pop[res] -= 1
            res = self._heapq[0]
        return res
