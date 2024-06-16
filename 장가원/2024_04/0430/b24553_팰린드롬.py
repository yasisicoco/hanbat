T = int(input())
for _ in range(T):
    N = int(input())
    # 상윤 승 : 0 / 승우 승 : 1
    res = 0
    if N % 10 == 0:
        res = 1
    print(res)