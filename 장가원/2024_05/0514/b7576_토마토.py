from sys import stdin; input = stdin.readline
from collections import deque
di = [0, 0, 1, -1]
dj = [1, -1, 0, 0]

def bfs():
    q = deque()
    for n in range(N):
        for m in range(M):
            # 익은 토마토
            if arr[n][m] == 1:
                q.append([n, m])
                res[n][m] = 0
                visited[n][m] = True
    while q:
        ci, cj = q.popleft()
        for k in range(4):
            ni = ci + di[k]
            nj = cj + dj[k]
            if 0<=ni<N and 0<=nj<M and res[ni][nj] == -1 and arr[ni][nj] == 0 and not visited[ni][nj]:
                visited[ni][nj] = True
                res[ni][nj] = res[ci][cj] + 1
                arr[ni][nj] = 1
                q.append([ni, nj])

M, N = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]
res = [[-1] * M for _ in range(N)]
visited = [[False] * M for _ in range(N)]

bfs()

# 다 익게 되는 최소 일수
day = 0
# arr 중 0이 존재하면 -1 반환
for i in range(N):
    for j in range(M):
        if not arr[i][j]:
            day = -1
            break
# 정답 출력
if day == -1:
    print(day)
else:
    day = max(map(max, res))
    print(day)
