from collections import deque
T = int(input())
for t in range(T):
    ps = deque(input())
    ans = 'YES'
    stack = deque()
    while ps:
        p = ps.popleft()
        if p == '(':
            stack.append(p)
        else:
            if not stack:
                ans = 'NO'
                break
            stack.popleft()
    if stack:
        ans = 'NO'
    print(ans)