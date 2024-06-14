from sys import stdin; input = stdin.readline
N = int(input())
lst = list(map(int, input().split()))
nge = [-1] * N
stack = []

for i in range(N):
    while stack and lst[stack[-1]] < lst[i]:
        nge[stack.pop()] = lst[i]
    stack.append(i)

print(*nge)