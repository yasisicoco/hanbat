di = [0, 0, 1, 1, 1, -1, -1, -1]
dj = [-1, 1, 0, -1, 1, 0, -1, 1]

from sys import stdin; input = stdin.readline
from collections import deque

def bfs(x, y):
    que = deque()
    que.append([x, y])
    arr[x][y] = 0
    while que:
        qi, qj = que.popleft()
        for k in range(8):
            ni = qi + di[k]
            nj = qj + dj[k]
            if 0<=ni<h and 0<=nj<w:
                if arr[ni][nj] == 1:
                    arr[ni][nj] = 0
                    que.append([ni, nj])

while True:
    w, h = map(int, input().split())
    if w == 0 and h == 0:
        exit()
    arr = [list(map(int, input().split())) for _ in range(h)]

    island = 0
    for i in range(h):
        for j in range(w):
            if arr[i][j] == 1:
                bfs(i, j)
                island += 1
    print(island)
