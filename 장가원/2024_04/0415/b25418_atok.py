from sys import stdin; input = stdin.readline
A, K = map(int, input().split())

# +1, *2 -> -1, /2
cnt = 0
while A < K:
    if K % 2 == 0:
        K //= 2
        cnt += 1
        if A > K:
            K *= 2
            K -= 1
    else:
        K -= 1
        cnt += 1

print(cnt)