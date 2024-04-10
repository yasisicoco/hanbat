def lotto(x):
    if x == 6:
        if choice == sorted(choice):
            print(*choice)

    for i in range(x, len(num)):
        if num[i] not in choice:
            choice.append(num[i])
            lotto(x + 1)
            choice.pop()

while True:

    k, *num = map(int, input().split())

    if k == 0:
        exit()

    choice = []
    lotto(0)
    print()