# 동 남
di = [0, 1]
dj = [1, 0]

def bitcoin(i, j):
    global ans
    visited[i][j] = 1
    if i == M - 1 and j == N - 1:
        ans = 'Yes'
        return ans
    for k in range(2):
        ni = i + di[k]
        nj = j + dj[k]
        if 0 <= ni < M and 0 <= nj < N:
            if dosi[ni][nj] == 1 and visited[ni][nj] == 0:
                bitcoin(ni, nj)

N, M = map(int, input().split())
dosi = [list(map(int, input().split())) for _ in range(M)]
visited = [[0] * N for _ in range(M)]
ans = 'No'
bitcoin(0, 0)
print(ans)