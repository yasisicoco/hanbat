from sys import stdin; input = stdin.readline
N = int(input())
time = list(map(int, input().split()))

SUM = 0
for i in range(N-1, -1, -1):
    MIN = min(time)
    SUM += time.pop(time.index(MIN)) * (i + 1)

print(SUM)


'''
5
3 1 4 3 2
'''