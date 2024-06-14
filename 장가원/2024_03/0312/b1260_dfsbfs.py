from collections import deque
def dfs(start):
    visited[start] = 1
    print(start, end=' ')
    for s in adjl[start]:
        if visited[s] == 0:
            visited[s] = 1
            dfs(s)
def bfs(start):
    queue = deque()
    queue.append(start)
    visited_bfs[start] = 1
    while queue:
        q = queue.popleft()
        print(q, end=' ')
        for s in adjl[q]:
            if visited_bfs[s] == 0:
                visited_bfs[s] = 1
                queue.append(s)

N, M, V = map(int, input().split())
# 인접 리스트
adjl = [[] for _ in range(N + 1)]
# 방문 리스트
visited = [0] * (N + 1)
visited_bfs = [0] * (N + 1)
for _ in range(M):
    u, v = map(int, input().split())
    adjl[u].append(v)
    adjl[v].append(u) # 양방향

for i in range(N + 1):
    adjl[i].sort()

dfs(V)
print()
bfs(V)
