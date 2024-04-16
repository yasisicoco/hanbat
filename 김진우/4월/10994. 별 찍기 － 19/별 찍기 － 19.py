def star(n, r, c):
    leng = (4*n)-3
    
    if leng == 1:
        arr[r][c] = "*" # 중앙
        return

    for i in range(leng):
        arr[r][c+i] = "*"
        arr[r+i][c] = "*"
        arr[r+(leng-1)][c+i] = "*"
        arr[r+i][c+(leng-1)] = "*"
    star(n-1, r+2, c+2)
        
        
N = int(input())
leng = (4*N)-3
arr = [[' ']*leng for _ in range(leng)]
star(N, 0, 0)
for line in arr:
    print(*line, sep='')