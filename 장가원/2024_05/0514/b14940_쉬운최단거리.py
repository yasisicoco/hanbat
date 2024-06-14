from sys import stdin; input = stdin.readline
from collections import deque
di = [0, 0, 1, -1]
dj = [1, -1, 0, 0]

def bfs(a, b):
    q = deque()
    q.append([a, b])
    ans[a][b] = 0

    while q:
        ci, cj = q.popleft()
        for k in range(4):
            ni = ci + di[k]
            nj = cj + dj[k]
            if 0<=ni<n and 0<=nj<m and arr[ni][nj] and ans[ni][nj] == -1:
                    ans[ni][nj] = ans[ci][cj] + 1
                    q.append([ni, nj])

n, m = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(n)]
ans = [[-1] * m for _ in range(n)]

# 2 인 곳을 찾아 x, y 에 저장
x, y = 0, 0
for i in range(n):
    for j in range(m):
        if arr[i][j] == 2:
            x = i
            y = j
            # 2 였던 곳을 0 으로 대체
            arr[i][j] = 0
            break
# 2 인 곳에서 bfs 시작
bfs(x, y)

# arr 가 0인 곳은 ans 도 0 으로 입력
for i in range(n):
    for j in range(m):
        if not arr[i][j]:
            ans[i][j] = 0

for a in ans:
    print(*a)
