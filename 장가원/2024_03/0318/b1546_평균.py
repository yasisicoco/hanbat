from sys import stdin; input = stdin.readline
N = int(input())
scores = list(map(int, input().split()))
MAX = max(scores)
SUM = 0
for score in scores:
    SUM += (score / MAX) * 100
print(SUM / N)