from sys import stdin; input = stdin.readline
N, M = map(int, input().split())
arr1 = [input() for _ in range(N)]
arr2 = [input() for _ in range(M)]
arr3 = arr1 + arr2
set_arr3 = set(arr3)

for i in set_arr3:
    if i in arr3:
        arr3.remove(i)

print(len(arr3))
arr3 = sorted(arr3)
for i in range(len(arr3)):
    print(arr3[i], end='')