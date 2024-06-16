from sys import stdin; input = stdin.readline
A, B, C = map(int, input().split()) # 각 기술 난이도
N = int(input())    # 동아리 수
MAX = 0
for _ in range(N):
    score = 0
    for i in range(3):
        a, b, c = map(int, input().split()) # 각 기술 사용 횟수
        score += A * a + B * b + C * c
    MAX = max(MAX, score)
print(MAX)