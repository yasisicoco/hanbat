while True:
    number = input()
    if number == '0':
        exit()

    N = len(number)
    ans = 'yes'
    for i in range(N//2):
        if number[i] != number[N - i - 1]:
            ans = 'no'
    print(ans)