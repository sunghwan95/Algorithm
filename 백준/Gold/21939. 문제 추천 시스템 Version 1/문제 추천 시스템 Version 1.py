import sys
import heapq
from collections import defaultdict

input = sys.stdin.readline

N = int(input())
hard_order, easy_order = [], []
solved_orders = defaultdict(bool)

for _ in range(N):
    order, difficulty = map(int, input().split())
    hard_order.append((-difficulty, -order))
    easy_order.append((difficulty, order))
    solved_orders[order] = False

heapq.heapify(hard_order)
heapq.heapify(easy_order)

M = int(input())

for _ in range(M):
    instructions = input().split()

    if instructions[0] == "add":
        order, difficulty = int(instructions[1]), int(instructions[2])
        heapq.heappush(hard_order, (-difficulty, -order))
        heapq.heappush(easy_order, (difficulty, order))

    elif instructions[0] == "recommend":
        output_method = int(instructions[1])

        if output_method == 1:
            while solved_orders[-hard_order[0][1]]:
                heapq.heappop(hard_order)
                solved_orders[-hard_order[0][1]] = False

            print(-hard_order[0][1])
        else:
            while solved_orders[easy_order[0][1]]:
                heapq.heappop(easy_order)
                solved_orders[easy_order[0][1]] = False

            print(easy_order[0][1])

    elif instructions[0] == "solved":
        order = int(instructions[1])
        solved_orders[order] = True
