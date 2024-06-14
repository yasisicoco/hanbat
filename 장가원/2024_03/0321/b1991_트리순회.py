import sys; input = sys.stdin.readline
'''
A ~ Z : 65 ~ 90
'''
def pre(root):
    if root:
        print(chr(root + 64), end='')
        pre(left[root])
        pre(right[root])

def inorder(root):
    if root:
        inorder(left[root])
        print(chr(root + 64), end='')
        inorder(right[root])

def post(root):
    if root:
        post(left[root])
        post(right[root])
        print(chr(root + 64), end='')

N = int(input())

right = [0] * (N + 1)
left = [0] * (N + 1)
# parent = [0] * (N + 1)

# A가 root node
for _ in range(N):
    nodes = list(input().split())
    i = ord(nodes[0]) - 64
    # 왼쪽 자식 노드
    if nodes[1] != '.':
        o = ord(nodes[1]) - 64
        left[i] = o
        # parent[o] = i
    # 오른쪽 자식 노드
    if nodes[2] != '.':
        o = ord(nodes[2]) - 64
        right[i] = o
        # parent[o] = i

# print(*right)
# print(*left)

pre(1)
print()
inorder(1)
print()
post(1)