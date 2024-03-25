N = int(input())


cnt = 0
while N > 0:
    if N % 3 == 0 and not N % 5 == 0: # 3으로 나누어지면서 5로 나누어지지 않을 때
        N -= 3
        cnt += 1
    elif N > 5:
        N -= 5
        cnt += 1
    elif N % 5 == 0: # 5로 나누어진다면
        N -= 5
        cnt += 1
    elif N % 3 == 0: # 3으로 나누어진다면
        N -= 3
        cnt += 1
    elif N % 5 == 3: # 5로 나누는데 나머지가 3이라면
        N -= 5
    elif 0 < N <= 4:
        N = -1
        break
        
        
if N == -1:
    print(N)
else:
    print(cnt)