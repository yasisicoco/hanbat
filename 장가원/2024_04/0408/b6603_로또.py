from sys import stdin; input = stdin.readline
while True:
    lst = list(map(int, input().split()))
    if lst[0] == 0: exit()
    k, S = lst[0], lst[1:]
    # S 중, 6개의 숫자로 만들 수 있는 조합 오름차순으로 모두 출력
    def comb(lotto):
        if len(lotto) == 6:
            print(*lotto)
            return

        start_idx = 0
        if lotto:
            start_idx = S.index(lotto[-1]) + 1
        for num in range(start_idx, k):
            lotto.append(S[num])
            comb(lotto)
            lotto.pop()
    comb([])
    print()
