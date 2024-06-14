import sys; input = sys.stdin.readline
sys.setrecursionlimit(10**6)
di = [0, 1, 0, -1]
dj = [1, 0, -1, 0]

def dfs(a, b):
    for k in range(4):
        ni = a + di[k]
        nj = b + dj[k]
        if 0<=ni<N and 0<=nj<N and not visited[ni][nj] and arr[ni][nj] > h:
            visited[ni][nj] = 1
            dfs(ni, nj)

N = int(input())    # 2 이상 100 이하
arr = [list(map(int, input().split())) for _ in range(N)]   # 각 높이: 1 이상 100 이하
min_height = min(map(min, arr))
max_height = max(map(max, arr))
M = 1   # 안전영역 최대 개수
for h in range(min_height, max_height + 2):     # 높이
    visited = [[0] * N for _ in range(N)]
    cnt = 0
    for i in range(N):
        for j in range(N):
            if arr[i][j] > h and not visited[i][j]:
                visited[i][j] = 1
                cnt += 1
                dfs(i, j)
    M = max(M, cnt)
print(M)
