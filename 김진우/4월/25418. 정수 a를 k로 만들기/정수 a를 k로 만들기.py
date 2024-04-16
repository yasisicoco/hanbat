from collections import deque

def calc(start, cnt):
    global ans
    
    q = deque()
    q.append([start, cnt])

    while q:
        start, cnt = q.popleft()
        if start == K:
            ans = cnt
            break
        if start > K:
            continue
        
        if visited[start] == 1:
            continue
        visited[start] = 1
        q.append([start+1, cnt+1])
        q.append([start*2, cnt+1])


A, K = map(int, input().split())
visited = [0] * 1000001
ans = 1e9
calc(A, 0)
print(ans)