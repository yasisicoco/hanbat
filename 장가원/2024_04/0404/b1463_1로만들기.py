from sys import stdin; input = stdin.readline
N = int(input())
num = N
cnt1 = cnt2 = 0
while N > 1:
    if N % 3 == 0:
        N //= 3
    elif N % 2 == 0:
        N //= 2
    else:
        N -= 1
    cnt1 += 1

while num > 1:
    if num % 3 == 0:
        num //= 3
    else:
        num -= 1
    cnt2 += 1

print(min(cnt1, cnt2))


'''
반례
40 -> 5
41 -> 6
'''

