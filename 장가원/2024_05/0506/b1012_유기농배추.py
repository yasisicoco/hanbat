from sys import stdin; input = stdin.readline
di = [0, 0, 1, -1]
dj = [1, -1, 0, 0]

def dfs(a, b):
    for k in range(4):
        ni = a + di[k]
        nj = b + dj[k]
        if 0<=ni<N and 0<=nj<M and arr[ni][nj]:
            arr[ni][nj] = 0
            dfs(ni, nj)

T = int(input())
for _ in range(T):
    M, N, K = map(int, input().split())
    arr = [[0] * M for _ in range(N)]
    for _ in range(K):
        x, y = map(int, input().split())
        arr[y][x] = 1
    # visited = [[0] * M for _ in range(N)]
    cnt = 0
    for i in range(N):
        for j in range(M):
            if arr[i][j] == 1:
                arr[i][j] = 0
                dfs(i, j)
                cnt += 1
    print(cnt)