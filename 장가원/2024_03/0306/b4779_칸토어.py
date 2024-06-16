def cantor(start, num):
    if num == 1:
        return
    for i in range(start + num // 3, start + (num // 3) * 2):
        lines[i] = ' '
    cantor(start, num // 3)        # 왼쪽
    cantor(start + (num // 3) * 2, num // 3)    # 오른쪽
    return lines

while True:
    try:
        N = int(input())    # 0 ~ 12
        num = 3 ** N
        lines = ['-'] * num
        cantor(0, num)
        print(''.join(lines))
    except EOFError:
        break

