N = int(input())
num = 4 * (N - 1) + 1
stars = [[' '] * num for _ in range(num)]

for k in range(0, num, 2):
    if num - k > k:
        for l in range(k, num - k):
            stars[k][l] = '*'
            stars[l][k] = '*'
    else:
        for l in range(num - k, k + 1):
            stars[k][l] = '*'
            stars[l][k] = '*'
for star in stars:
    print(*star, sep='')
