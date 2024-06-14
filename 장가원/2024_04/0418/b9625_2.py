K = int(input())
# B -> BA, A -> B
A = 1
B = 0
for _ in range(K):
    new_A = 0
    new_B = 0
    if A:
        new_B = A
        A = 0
    if B:
        A += B
    B += new_B
print(A, B)

'''
B
BA
BAB
BABBA
'''
