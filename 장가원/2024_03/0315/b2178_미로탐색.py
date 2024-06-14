# delta & bfs
from collections import deque
di = [0, 1, 0, -1]
dj = [1, 0, -1, 0]

def move():
    q = deque()
    q.append([0, 0])
    visited[0][0] = 1
    while q:
        [i, j] = q.popleft()
        for k in range(4):
            ni = i + di[k]
            nj = j + dj[k]
            if 0 <= ni < N and 0 <= nj < M:
                if miro[ni][nj] == 1 and visited[ni][nj] == 0:
                    q.append([ni, nj])
                    visited[ni][nj] = visited[i][j] + 1
                    if ni == N - 1 and nj == M - 1:
                        return visited[ni][nj]

N, M = map(int, input().split())
miro = [list(map(int, input())) for _ in range(N)]
visited = [[0] * M for _ in range(N)]

print(move())


