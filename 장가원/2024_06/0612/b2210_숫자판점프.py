import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)

di = [0, 0, 1, -1]
dj = [1, -1, 0, 0]

def dfs(a, b):
    global number
    if len(number) == 6:
        # numbers 에 없는 수일 경우, append
        if number not in numbers:
            numbers.append(number)
        return

    for k in range(4):
        ni = a + di[k]
        nj = b + dj[k]
        if 0<=ni<5 and 0<=nj<5:
            number += arr[ni][nj]
            dfs(ni, nj)
            # number 마지막 하나 뺴야함
            number = number[:-1]

arr = [list(input().split()) for _ in range(5)]
numbers = []

for i in range(5):
    for j in range(5):
        number = ''
        number += arr[i][j]
        dfs(i, j)

print(len(numbers))
