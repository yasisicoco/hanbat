from sys import stdin; input = stdin.readline
N = int(input())
buildings = []
for _ in range(N):
    buildings.append(int(input()))

# -> 이 방향으로 바라봄
# 자기보다 낮은 빌딩만 볼 수 있음

num = []
for i in range(N):
    cnt = 0
    for j in range(i + 1, N):
        if buildings[i] > buildings[j]:
            cnt += 1
        else:
            break
    num.append(cnt)
print(sum(num))
# 4% -> 시간초과

# i = 0
# low = []
# while i < N:
#     cnt = 0
#     for j in range(i + 1, N):
#         if buildings[i] > buildings[j]:
#             cnt += 1
#         else:
#             break
#     low.append(cnt)
#     i += 1
# print(sum(low))
# 4% -> 시간초과
