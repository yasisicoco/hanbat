# 재귀
import sys; input = sys.stdin.readline
sys.setrecursionlimit(10**6)
# N : 상어 수, K : 먹을 수 있는 최대 수, T : 상어 최초 크기
N, K, T = map(int, input().split())
shark_sizes = list(map(int, input().split()))

# 자신의 크기보다 작은 상어만 먹 가능

# 큰 애들 부터 가져오기
shark_sizes.sort(reverse=True)
# print(shark_sizes)

def growing(size):
    global cnt, ans
    if cnt == K:
        ans = size
        return

    for i in range(len(shark_sizes)):
        if shark_sizes[i] < size:
            size += shark_sizes[i]
            shark_sizes.pop(i)
            cnt += 1
            growing(size)
            return

cnt = 0     # 먹은 수
ans = 0
growing(T)
# print(shark_sizes)

if ans == 0:
    ans = T
print(ans)

# for i in range(N):
#     if shark_sizes[i] < T:
#         T += shark_sizes[i]
#         shark_sizes.pop(i)
#         break

# 시간초과