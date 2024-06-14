N = 10000  # 생성자
lst = [i for i in range(1, 10001)]
for n in range(N):
    makeN = n
    num = str(n)
    for i in num:
        makeN += int(i)
    if makeN in lst:
        lst.remove(makeN)

for i in range(len(lst)):
    print(lst[i])