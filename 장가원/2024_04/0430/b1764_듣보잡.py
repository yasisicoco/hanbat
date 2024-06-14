from sys import stdin; input = stdin.readline
N, M = map(int, input().split())
arr1 = [input() for _ in range(N)]
arr2 = [input() for _ in range(M)]
arr3 = []
for i in range(N):
    if arr1[i] in arr2:
        arr3.append(arr1[i])

print(len(arr3))
arr3 = sorted(arr3)
for i in range(len(arr3)):
    print(arr3[i], end='')