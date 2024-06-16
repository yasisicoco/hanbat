import sys; input = sys.stdin.readline
A, B = map(int, input().split())
ans = 1
# 곱하기 2
# 수의 오른쪽에 1 추가
while B > A:
    if B % 10 == 1:
        ans += 1
        B //= 10
    elif B % 2 == 0:
        ans += 1
        B //= 2
    else:
        break

if A == B:
    print(ans)
else:
    print(-1)