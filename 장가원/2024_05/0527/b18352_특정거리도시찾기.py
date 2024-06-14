from sys import stdin; input = stdin.readline
from collections import deque
# 도시 : 1 ~ N번
# 단방향 도로 : 1 ~ M번
# 출발점 : X번 도시
# 최단 거리가 K인 도시 번호들 출력
N, M, K, start = map(int, input().split())
adjl = [[] for _ in range(N + 1)]
visited = [False] * (N + 1)
distance = [int(1e6)] * (N + 1)
for _ in range(M):
    A, B = map(int, input().split())
    adjl[A].append(B)   # 단방향

def bfs(s):
    q = deque()
    q.append(s)
    visited[s] = True
    distance[s] = 0

    while q:
        x = q.popleft()
        for i in adjl[x]:
            if not visited[i]:
                visited[i] = True
                distance[i] = min(distance[i], distance[x] + 1)
                q.append(i)
bfs(start)

ans = []
flag = False
for d in range(N + 1):
    if distance[d] == K:
        ans.append(d)
        flag = True
if not flag:
    ans.append(-1)
ans.sort()
for a in ans:
    print(a)