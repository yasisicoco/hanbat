import sys; input = sys.stdin.readline
sys.setrecursionlimit(10**6)
di = [0, 0, 1, -1]
dj = [1, -1, 0, 0]

def dfs(a, b, col):
    for k in range(4):
        ni = a + di[k]
        nj = b + dj[k]
        if 0<=ni<N and 0<=nj<N and not visited[ni][nj] and arr[ni][nj] == col:
            visited[ni][nj] = True
            dfs(ni, nj, col)

N = int(input())
arr = [list(input()) for _ in range(N)]

ans = 0     # 일반인 구역 수
visited = [[False] * N for _ in range(N)]
for i in range(N):
    for j in range(N):
        if not visited[i][j]:
            visited[i][j] = True
            ans += 1
            dfs(i, j, arr[i][j])

ans_s = 0   # 적록색약인 구역 수
visited = [[False] * N for _ in range(N)]
# G 전부 R 로 바꾸기
for i in range(N):
    for j in range(N):
        if arr[i][j] == 'G':
            arr[i][j] = 'R'
for i in range(N):
    for j in range(N):
        if not visited[i][j]:
            visited[i][j] = True
            ans_s += 1
            dfs(i, j, arr[i][j])

print(ans, ans_s)
