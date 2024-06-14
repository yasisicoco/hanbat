from sys import stdin; input = stdin.readline
from collections import deque
di = [0, 0, 1, -1]
dj = [1, -1, 0, 0]
# 인접한 두 나라 인구 차가 L 이상 R 이하일때 국경선 열림(연합)

def bfs(a, b):
    q = deque()
    q.append([a, b])
    visited[a][b] = True
    # 연합
    union = [[a, b]]
    s = arr[a][b]   # 연합 인구 수 합

    while q:
        ci, cj = q.popleft()
        for k in range(4):
            ni = ci + di[k]
            nj = cj + dj[k]
            if 0<=ni<N and 0<=nj<N and not visited[ni][nj]:
                if L <= abs(arr[ni][nj] - arr[ci][cj]) <= R:
                    visited[ni][nj] = True
                    q.append([ni, nj])
                    union.append([ni, nj])
                    s += arr[ni][nj]
    num = s // len(union)
    for a, b in union:
        arr[a][b] = num
    return len(union)   # 연합 수

N, L, R = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]
changed = True  # 연합 1개 이상인지
day = 0     # 며칠 동안 인구 이동?

while changed:
    changed = False
    visited = [[False] * N for _ in range(N)]
    for i in range(N):
        for j in range(N):
            if not visited[i][j]:
                if bfs(i, j) > 1:   # 연합 수
                    changed = True
    day += 1
print(day-1)