N = int(input())
recur = 4 * N - 3
starry = [[' '] * recur for _ in range(recur)]

for idx in range(0, recur, 2):
    if recur - idx > recur // 2:
        for r in range(idx, recur - idx):
            starry[idx][r] = '*'
            starry[r][idx] = '*'
    else:
        for c in range(recur - idx, idx + 1):
            starry[idx][c] = '*'
            starry[c][idx] = '*'

for i in range(recur):
    print(''.join(starry[i]))