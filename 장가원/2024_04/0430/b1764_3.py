from sys import stdin; input = stdin.readline
N, M = map(int, input().split())
arr1 = set(input() for _ in range(N))
arr3 = []
for i in range(M):
    compare = input()
    if compare in arr1:
        arr1.remove(compare)
        arr3.append(compare)

print(len(arr3))
arr3 = sorted(arr3)
for i in range(len(arr3)):
    print(arr3[i], end='')