string = input()
bomb = input()
b = len(bomb)
ans = []
for s in string:
    ans.append(s)
    if ''.join(ans[-b:]) == bomb:
        for _ in range(b):
            ans.pop()

if not ans:
    print('FRULA')
else:
    print(''.join(ans))
