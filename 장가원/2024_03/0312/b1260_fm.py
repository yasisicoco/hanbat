def dfs(start):
    visited[start] = 1
    print(start, end=' ')
    for s in adjl[start]:
        if visited[s] == 0:
            visited[s] = 1
            dfs(s)

def bfs(start):
    Q = []
    Q.append(start)
    visited_bfs[start] = 1
    while Q:
        s = Q.pop(0)
        print(s, end=' ')
        for i in adjl[s]:
            if visited_bfs[i] == 0:
                Q.append(i)
                visited_bfs[i] = 1 + visited_bfs[s]

N, M, V = map(int, input().split())
# 인접 리스트
adjl = [[] for _ in range(N + 1)]
# 방문 리스트
visited = [0] * (N + 1)
visited_bfs = [0] * (N + 1)
for _ in range(M):
    u, v = map(int, input().split())
    adjl[u].append(v)
    adjl[v].append(u) # 무향

for i in range(N + 1):
    adjl[i].sort()

dfs(V)
print()
bfs(V)