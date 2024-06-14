di = [0, 0, 1, -1]
dj = [1, -1, 0, 0]

def dfs(a, b):
    global cnt
    for k in range(4):
        ni = a + di[k]
        nj = b + dj[k]
        if 0<=ni<N and 0<=nj<N and arr[ni][nj] and not visited[ni][nj]:
            visited[ni][nj] = 1
            cnt += 1
            dfs(ni, nj)

N = int(input())
arr = [list(map(int, input())) for _ in range(N)]
visited = [[False] * N for _ in range(N)]
home = []
danji = 0
for i in range(N):
    for j in range(N):
        cnt = 1
        if arr[i][j] and not visited[i][j]:
            danji += 1
            visited[i][j] = 1
            dfs(i, j)
            home.append(cnt)

print(danji)
home.sort()
for h in home:
    print(h)