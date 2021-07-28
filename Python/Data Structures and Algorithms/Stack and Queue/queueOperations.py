# Exercise link: https://github.com/codebasics/data-structures-algorithms-python/blob/master/data_structures/6_Queue/Exercise/binary_numbers.py
from collections import deque
q = deque()

# Problem 2!
q.appendleft("1")

for i in range(10):
    front = q[-1]
    print(front)
    q.appendleft(front + "0")
    q.appendleft(front + "1")

    print(q.pop())

    