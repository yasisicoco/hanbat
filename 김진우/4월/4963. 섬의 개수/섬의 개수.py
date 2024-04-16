from collections import deque
# from pprint import pprint
import sys
sys.setrecursionlimit(10**6) 
input = sys.stdin.readline
di = [0, 1, -1, 0, 1, 1, -1, -1]
dj = [1, 0, 0, -1, 1, -1, 1, -1]
def bfs(si, sj):
    q = deque()
    q.append([si, sj])
    visited[si][sj] = True
    while q:
        ci, cj = q.popleft()
        for k in range(8):
            ni = ci + di[k]
            nj = cj + dj[k]
            if 0 <= ni < h and 0 <= nj < w and arr[ni][nj] == 1 and not visited[ni][nj]:
                visited[ni][nj] = True
                q.append([ni,nj])

while True:
    w, h = map(int, input().split())
    if w == 0 and h == 0:
        break
    arr = []
    for _ in range(h):
        arr.append(list(map(int, input().split())))
    visited = [[False] * w for _ in range(h)]
    cnt = 0
    for i in range(h):
        for j in range(w):
            if arr[i][j] == 1 and not visited[i][j]:
                bfs(i, j)
                cnt += 1
    print(cnt)