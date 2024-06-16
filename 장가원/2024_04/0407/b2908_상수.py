from sys import stdin; input = stdin.readline
A, B = map(list, input().split())
A.reverse()
resA = int(''.join(A))
B.reverse()
resB = int(''.join(B))
if resA > resB:
    print(resA)
else:
    print(resB)
