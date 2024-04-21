# 울타리안에 들어갔을 때, v와 k의 수를 센다.
# v와 k의 수가 같거나 v가 크면 v만 출력,
# k가 크면 k 만 출력한다.
# #를 만나면 못지나가고 . 은 빈 공간이므로 지나갈 수 있다.
import sys
sys.setrecursionlimit(10**6)

di = [0, 1, -1, 0]
dj = [1, 0, 0, -1]

def dfs(si, sj):
    global v_val, k_val
    
    for k in range(4):
        ni = si + di[k]
        nj = sj + dj[k]
        if 0 <= ni < R and 0 <= nj < C and visited[ni][nj] == False and arr[ni][nj] != '#':
            visited[ni][nj] = True
            if arr[ni][nj] == 'v':
                v_val += 1            
            elif arr[ni][nj] == 'k':
                k_val += 1
            dfs(ni, nj)

                
R, C = map(int, input().split())
arr = [input() for _ in range(R)]
visited = [[False] * C for _ in range(R)]

v_val_ans = 0 # 늑대
k_val_ans = 0 # 양
for r in range(R):
    v_val = 0
    k_val = 0
    for c in range(C):
        if visited[r][c] or arr[r][c] == '#':
            continue
        visited[r][c] = True
        if arr[r][c] == 'v':
            v_val += 1
        elif arr[r][c] == 'k':
            k_val += 1
        dfs(r, c)
        
        if v_val < k_val:
            k_val_ans += k_val
        elif v_val >= k_val:
            v_val_ans += v_val
        v_val = 0
        k_val = 0

print(f'{k_val_ans} {v_val_ans}')