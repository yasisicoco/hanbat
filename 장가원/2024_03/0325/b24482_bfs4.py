from sys import stdin, setrecursionlimit; input = stdin.readline
setrecursionlimit(10**6)
def dfs(start, depth):
    visited[start] = depth

    for s in sorted(adjl[start], reverse=True): # 인접정점 내림차순 방문
        if visited[s] == -1:    # 방문하지 않았다면
            dfs(s, depth + 1)

# 모든 노드의 깊이 구하기 -> visited에 저장
N, M, R = map(int, input().split())
adjl = [[] for _ in range(N + 1)]
visited = [-1] * (N + 1)    # 방문되지 않은 노드의 깊이 : -1 로 초기화
for _ in range(M):
    u, v = map(int, input().split())
    adjl[u].append(v)
    adjl[v].append(u)   # 무방향

dfs(R, 0)   # 시작 정점 R의 깊이 : 0

print(*visited[1:], sep='\n')
