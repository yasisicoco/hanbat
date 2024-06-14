from sys import stdin; input = stdin.readline
# N : 국가 수, K : 등수 구할 국가
N, K = map(int, input().split())
# 국가, 금 수, 은 수, 동 수
medals = [list(map(int, input().split())) for _ in range(N)]
medals.sort(key=lambda x: (x[1], x[2], x[3]), reverse=True)

# print(medals)

# K 의 메달 수 : [금, 은, 동]
k_medal = [0] * 3
for i in range(N):
    if medals[i][0] == K:
        k_medal = medals[i][1:]

# 등수 구하기
# 등수 = 자신보다 더 잘한 나라 수 + 1
grade = 1
for i in range(N):
    if medals[i][1:] == k_medal:
        break
    else:
        grade += 1

print(grade)

# 100점