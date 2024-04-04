from collections import deque

N = int(input())
integer = deque([N])
visited = [0] * (N + 1)

while True:

    x = integer.popleft()

    if x == 1:
        print(visited[x])
        break

    if x % 3 == 0 and visited[x // 3] == 0:
        visited[x // 3] = visited[x] + 1
        integer.append(x // 3)
    if x % 2 == 0 and visited[x // 2] == 0:
        visited[x // 2] = visited[x] + 1
        integer.append(x // 2)
    if visited[x - 1] == 0:
        visited[x - 1] = visited[x] + 1
        integer.append(x - 1)