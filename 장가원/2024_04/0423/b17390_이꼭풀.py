from sys import stdin; input = stdin.readline
# N : 수열 A의 길이, Q : 질문 수
N, Q = map(int, input().split())
A = list(map(int, input().split()))
A.sort()

S = [0] * (N + 1)
for i in range(1, N+1):
    S[i] = S[i-1] + A[i-1]

for _ in range(Q):
    L, R = map(int, input().split())
    print(S[R] - S[L-1])
