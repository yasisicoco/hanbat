from sys import stdin; input = stdin.readline
N = int(input())
lst = []
for _ in range(N):
    age, name = input().split()
    age = int(age)
    lst.append([age, name])
lst.sort(key=lambda x: x[0])

for l in lst:
    print(*l)