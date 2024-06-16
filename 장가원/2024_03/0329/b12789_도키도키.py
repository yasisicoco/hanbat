from sys import stdin; input = stdin.readline
N = int(input())
students = list(map(int, input().split()))  # 현재 줄

ans = 'Sad'
stack = []  # 한 명씩 설 수 있는 공간
res = []    # 간식 받는 곳

for i in range(N):  # 0 ~ N-1
    while stack and students[i] > stack[-1]:
        res.append(stack.pop())
    if i == N - 1:
        res.append(students[i])
        break

    if students[i] > students[i+1]:
        stack.append(students[i])
    else:
        res.append(students[i])

# stack에서 res로 이동시키기
while stack:
    res.append(stack.pop())

# 끝까지 번호순으로 받으면 Nice 아니면 Sad
for i in range(N - 1):
    if res[i] > res[i + 1]:
        break
else:
    ans = 'Nice'

# print(*res)
print(ans)


'''
5
4 5 1 3 2
'''