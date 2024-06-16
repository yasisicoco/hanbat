from sys import stdin; input = stdin.readline
# N : 국가 수, K : 등수 구할 나라
N, K = map(int, input().split())
# 국가, 금 수, 은 수, 동 수
lst = [list(map(int, input().split())) for _ in range(N)]
lst.sort(key=lambda x: (x[1], x[2], x[3]), reverse=True)

# rank 딕셔너리에 저장 -> 등수 : 나라 번호
rank = {}
for i in range(N):
    rank[lst[i][0]] = i + 1

# 동점인 경우 처리
equal = 0
for i in range(N - 1):
    if lst[i][1:] == lst[i+1][1:]:
        equal += 1
    else:
        rank[lst[i][0]] -= equal
        equal = 0
for i in range(N):
    if lst[i][0] == K:
        print(rank[K])

# 45점