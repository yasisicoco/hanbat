from sys import stdin; input = stdin.readline
n = int(input())
D = []
T = []
for _ in range(n):
    d, t = map(int, input().split())
    D.append(d)
    T.append(t)

T_MAX = day = 0
while T:
    T_MAX = max(T)
    idx = T.index(T_MAX)
    if day != 0 and T_MAX >= day:
        day -= D[idx]
    else:
        day = T_MAX - D[idx]
    T.pop(idx)
    D.pop(idx)

print(day)