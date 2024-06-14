# 시간초과.
string = input()
bomb = input()
b = len(bomb)

idx = string.find(bomb)
while idx >= 0:
    string = list(string)
    for i in range(b):
        string.pop(idx)
    string = ''.join(string)
    idx = string.find(bomb)

if not string:
    print('FRULA')
else:
    print(string)
