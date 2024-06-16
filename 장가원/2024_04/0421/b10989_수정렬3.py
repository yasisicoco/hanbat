from sys import stdin; input = stdin.readline
N = int(input())
numbers = [0] * 10001
for _ in range(N):
    numbers[int(input())] += 1
for i in range(len(numbers)):
    if numbers[i]:
        for _ in range(numbers[i]):
            print(i)
# 메모리 초과 주의 문제