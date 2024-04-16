def recur(cur):
    if len(ans) == 6:
        print(*ans)
        return
    
    for i in range(cur, k):
        if visited[i]:
            continue
        visited[i] = 1
        ans.append(lst[i])
        recur(i)
        ans.pop()
        visited[i] = 0

while True:
    lst = list(map(int, input().split()))
    if len(lst) == 1:
        break
    k = lst[0]
    lst = lst[1:]

    ans = []
    visited = [0] * (k+1)
    recur(0)
    print()