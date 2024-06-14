# N: 블로그 시작하고 지난 일 수, X: 기간
N, X = map(int, input().split())
# N일 동안 방문자 수 (길이 N인 리스트)
visitors = list(map(int, input().split()))

sum_visitors = sum(visitors[:X])
visits = [sum_visitors]
for i in range(N - X):
    sum_visitors = sum_visitors - visitors[i] + visitors[i + X]
    visits.append(sum_visitors)
max_visitors = max(visits)

if max_visitors == 0:
    print('SAD')
else:
    print(max_visitors)
    print(visits.count(max_visitors))


# 시간초과
# visits = []
# for i in range(N - X + 1):
#     sum_visit = 0
#     for j in range(i, i + X):
#         sum_visit += visitors[j]
#     visits.append(sum_visit)
# max_visit = max(visits)
# if max_visit == 0:
#     print('SAD')
# else:
#     print(max_visit)
#     print(visits.count(max_visit))
