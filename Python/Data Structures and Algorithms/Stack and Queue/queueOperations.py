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

    