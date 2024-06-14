from sys import stdin; input = stdin.readline
while True:
    a, b, c = map(int, input().split())
    if a == 0 and b == 0 and c == 0:
        exit()
    result = "wrong"
    if a ** 2 + b ** 2 == c ** 2 or b ** 2 + c ** 2 == a ** 2 or c ** 2 + a ** 2 == b ** 2:
        result = "right"
    print(result)