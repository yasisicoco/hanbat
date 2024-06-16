from sys import stdin; input = stdin.readline
N, M = map(int, input().split())
trees = list(map(int, input().split()))

start, end = 0, max(trees)
mid = end // 2

while end >= start:
    sum_tree = 0
    for tree in trees:
        if tree > mid:
            sum_tree += tree - mid
    # if sum_tree == M:
    #     print(mid)
    #     break
    if sum_tree >= M:
        start = mid + 1
    else:   # sum_tree < M
        end = mid - 1
    mid = (end + start) // 2
print(end)

# 완

# def cut(height, sum_tree):
#     # if n == N:
#     #     return
#     if sum_tree == M:
#         print(height)
#         return
#     for tree in trees:
#         cut(height - 1, sum_tree + tree - height)
#         cut(height - 1, sum_tree)
#
# cut(max(trees) - 1, 0)


# 설정 가능한 높이 최대값 구하기
# height = max(trees) - 1
# while True:
#     sum_tree = 0
#     for tree in trees:
#         sum_tree += tree - height
#     if sum_tree == M:
#         print(height)
#         break
#     height -= 1