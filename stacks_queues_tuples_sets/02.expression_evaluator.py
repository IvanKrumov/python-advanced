from collections import deque

user_input = input().split()

queue = deque()


def calculte(a: int, b: int, operator: str) -> int:
    if operator == "+":
        return a + b
    elif operator == "-":
        return a - b
    elif operator == "*":
        return a * b
    elif operator == "/":
        return a // b


for c in user_input:
    if c not in "+-*/":
        queue.append(int(c))
    else:
        while len(queue) > 1:
            num_1 = queue.popleft()
            num_2 = queue.popleft()
            queue.appendleft(calculte(num_1, num_2, c))
            # if c == "+":
            #     queue.appendleft(num_1 + num_2)
            # elif c == "-":
            #     queue.appendleft(num_1 - num_2)
            # elif c == "*":
            #     queue.appendleft(num_1 * num_2)
            # elif c == "/":
            #     queue.appendleft(num_1 // num_2)

print(queue.popleft())
