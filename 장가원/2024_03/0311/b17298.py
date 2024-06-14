from sys import stdin; input = stdin.readline
N = int(input())
lst = list(map(int, input().split()))
nge = []

for i in range(N):
    for j in range(i+1, N):
        if i == N:
            nge.append(-1)
            break
        if lst[j] > lst[i]:
            nge.append(lst[j])
            break
    else:
        nge.append(-1)
print(*nge)


