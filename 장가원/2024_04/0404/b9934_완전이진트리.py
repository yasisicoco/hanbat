from sys import stdin; input = stdin.readline
K = int(input())
order = list(map(int, input().split()))
N = len(order)
tree = [[] for _ in range(K)]

def make_tree(start, end, level):
    mid = (start + end) // 2
    tree[level].append(order[mid])

    if start == end:
        return

    make_tree(start, mid - 1, level + 1)
    make_tree(mid + 1, end, level + 1)

make_tree(0, N-1, 0)
for t in tree:
    print(*t)

# start, end = 0, len(order) - 1
# mid = len(order) // 2
# print(order[mid])
# l_mid = r_mid = mid
# cnt = 1
# while cnt < len(order):
#     l_mid = (start + l_mid-1) // 2
#     r_mid = (r_mid+1 + end) // 2
#     print(order[l_mid], order[r_mid])
#     cnt += 2
