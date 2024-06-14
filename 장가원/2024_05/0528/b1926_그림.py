import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)
di = [0, 0, 1, -1]
dj = [1, -1, 0, 0]

def dfs(a, b):
    global area
    for k in range(4):
        ni = a + di[k]
        nj = b + dj[k]
        if 0<=ni<n and 0<=nj<m and arr[ni][nj] and not visited[ni][nj]:
            visited[ni][nj] = True
            area += 1
            dfs(ni, nj)

n, m = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(n)]
visited = [[False] * m for _ in range(n)]
# 그림 수, 가장 넓은 그림의 넓이
# 그림 수 = 0 -> 넓이 = 0
grim = 0
max_area = 0

for i in range(n):
    for j in range(m):
        if arr[i][j] and not visited[i][j]:
            visited[i][j] = True
            area = 1
            dfs(i, j)
            grim += 1
            max_area = max(area, max_area)

print(grim)
print(max_area)