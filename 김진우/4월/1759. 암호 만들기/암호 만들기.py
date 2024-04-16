def password(cur):
    
    if len(ans) == L:
        vow = 0
        con = 0
        for l in ans:
            if l in 'aeiou':
                vow += 1
            else:
                con += 1
        if vow >= 1 and con >= 2:
            print(*ans, sep='')
        return

    for i in range(cur, C):
        if visited[i]:
            return
        visited[i] = True
        ans.append(lst[i])
        password(i+1)
        visited[i] = False
        ans.pop()



L, C = map(int, input().split())
lst = list(input().split())
visited = [False for _ in range(C+1)]
lst.sort()
ans = []
password(0)
