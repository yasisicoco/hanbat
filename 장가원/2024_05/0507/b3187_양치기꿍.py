import sys; input = sys.stdin.readline
sys.setrecursionlimit(10**8)
di = [0, 0, 1, -1]
dj = [1, -1, 0, 0]

def dfs(a, b):
    global s_cnt, w_cnt
    for k in range(4):
        ni = a + di[k]
        nj = b + dj[k]
        if 0<=ni<R and 0<=nj<C and not visited[ni][nj] and arr[ni][nj] != '#':
            # 4방향 중 '#'이 나오면 중단, '.'이면 계속 진행해야 함.(visited, dfs())
            visited[ni][nj] = True
            if arr[ni][nj] == 'v':
                w_cnt += 1
            elif arr[ni][nj] == 'k':
                s_cnt += 1
            dfs(ni, nj)

R, C = map(int, input().split())
arr = [list(input()) for _ in range(R)]
visited = [[False] * C for _ in range(R)]
sheep = 0
wolf = 0
for i in range(R):
    for j in range(C):
        s_cnt = 0
        w_cnt = 0
        if arr[i][j] == 'v' and not visited[i][j]:
            visited[i][j] = True
            w_cnt += 1
            dfs(i, j)
        elif arr[i][j] == 'k' and not visited[i][j]:
            visited[i][j] = True
            s_cnt += 1
            dfs(i, j)

        if s_cnt > w_cnt:
            sheep += s_cnt
        else:
            wolf += w_cnt

print(sheep, wolf)
