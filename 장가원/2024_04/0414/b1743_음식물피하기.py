di = [0, 0, 1, -1]
dj = [1, -1, 0, 0]

from sys import stdin; input = stdin.readline
from collections import deque
# N x M -> K개 음식물
N, M, K = map(int, input().split())
arr = [[0] * M for _ in range(N)]
for _ in range(K):
    # 음식물 좌표
    c, r = map(int, input().split())
    arr[c-1][r-1] = 1

def bfs(x, y):
    global cnt
    que = deque()
    que.append((x, y))
    arr[x][y] = 0
    while que:
        qi, qj = que.popleft()
        for k in range(4):
            ni = qi + di[k]
            nj = qj + dj[k]
            if 0<=ni<N and 0<=nj<M:
                if arr[ni][nj] == 1:
                    arr[ni][nj] = 0
                    que.append((ni, nj))
                    cnt += 1
MAX = 0
for i in range(N):
    for j in range(M):
        if arr[i][j] == 1:
            cnt = 1
            bfs(i, j)
            MAX = max(MAX, cnt)
print(MAX)

