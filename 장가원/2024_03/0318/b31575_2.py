from collections import deque
# 동 남
di = [0, 1]
dj = [1, 0]

N, M = map(int, input().split())
coin = [list(map(int, input().split())) for _ in range(N)]
visited = [[0] * M for _ in range(N)]

def bit():
    q = deque()
    q.append([0, 0])
    visited[0][0] = 1
    while q:
        [i, j] = q.popleft()
        for k in range(2):
            ni = i + di[k]
            nj = j + dj[k]
            if 0 <= ni < N and 0 <= nj < M:
                if coin[ni][nj] == 1 and visited[ni][nj] == 0:
                    visited[ni][nj] = visited[i][j] + 1
                    q.append([ni, nj])
                    if [ni, nj] == [N - 1, M - 1]:
                        return 'Yes'
    return 'NO'

print(bit())

# 틀림
