N = int(input())
lst = list(map(int, input().split()))
lst.sort()
ans = 0
for i in range(N):
    k = sum(lst[0:i+1])
    ans += k
print(ans)