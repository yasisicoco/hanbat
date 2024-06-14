from sys import stdin; input = stdin.readline
N = int(input())

# dp : 최소 연산 횟수
dp = [0] * (N + 1)

# bottom-up (거꾸로)
for i in range(2, N + 1):   # dp[1] = 0 이니까 dp[2] 부터 시작.
    dp[i] = dp[i-1] + 1     # i - 1 : 1 빼기 -> cnt += 1

    if i % 3 == 0:
        dp[i] = min(dp[i], dp[i // 3] + 1)  # i // 3 : 3 나누기 -> cnt += 1
    if i % 2 == 0:
        dp[i] = min(dp[i], dp[i // 2] + 1)  # i // 2 : 2 나누기 -> cnt += 1

print(dp[N])

