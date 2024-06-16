# while문
from sys import stdin; input = stdin.readline
# N : 상어 수, K : 먹을 수 있는 최대 수, T : 상어 최초 크기
N, K, T = map(int, input().split())
shark_sizes = list(map(int, input().split()))
# 큰 애들 부터 가져오기
shark_sizes.sort(reverse=True)
# 자신의 크기보다 작은 상어만 먹 가능
cnt = 0
small = []
while cnt < K:
    if shark_sizes and shark_sizes[-1] < T:
        small.append(shark_sizes.pop())
    else:
        if small:
            T += small.pop()
            cnt += 1
        else:
            break
print(T)

# 맞