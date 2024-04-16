from collections import deque
A, K = map(int, input().split())
visited = [0] * 1000001

def makenum(A):

    q = deque()
    q.append((A, 0))
    visited[A] = 1

    while q:
        num, cnt = q.popleft()
        if num == K:
            print(cnt)
            return

        cnt += 1
        for a in (num * 2, num + 1):
            if a > K:
                continue
            if visited[a] == 0:
                visited[a] = 1
                q.append((a, cnt))

makenum(A)