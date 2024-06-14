from collections import deque
N, M = map(int, input().split())
positions = list(map(int, input().split()))

q = deque()
for i in range(1, N + 1):
    q.append(i)

# 1) popleft
# 2) popleft & append
# 3) pop & appendleft

ans = 0
for pos in positions:
    if pos == q[0]:    # 1번 연산
        q.popleft()
    else:
        while True:
            if q.index(pos) <= len(q) // 2:  # 2번 연산
                n = q.popleft()
                q.append(n)
                ans += 1
                if pos == q[0]:  # 1번 연산
                    q.popleft()
                    break
            else:   # 3번 연산
                n = q.pop()
                q.appendleft(n)
                ans += 1
                if pos == q[0]:  # 1번 연산
                    q.popleft()
                    break
print(ans)
