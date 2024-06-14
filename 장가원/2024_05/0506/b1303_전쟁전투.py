from sys import stdin; input = stdin.readline
di = [0, 0, 1, -1]
dj = [1, -1, 0, 0]

def dfs(a, b, col):
    global cnt
    for k in range(4):
        ni = a + di[k]
        nj = b + dj[k]
        if 0<=ni<M and 0<=nj<N and not visited[ni][nj] and arr[ni][nj] == col:
            visited[ni][nj] = 1
            cnt += 1
            dfs(ni, nj, col)

N, M = map(int, input().split())
arr = [list(input()) for _ in range(M)]
visited = [[0] * N for _ in range(M)]

white = 0
blue = 0
for i in range(M):
    for j in range(N):
        cnt = 1
        if arr[i][j] == 'W' and not visited[i][j]:
            visited[i][j] = 1
            dfs(i, j, 'W')
            white += cnt**2
        elif arr[i][j] == 'B' and not visited[i][j]:
            visited[i][j] = 1
            dfs(i, j, 'B')
            blue += cnt**2
print(white, blue)
