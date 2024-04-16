N = int(input())
arr = list(map(int, input().split()))
add, sub, mul, div = map(int, input().split())

max_val = -int(1e9)
min_val = int(1e9)

def dfs(idx, result, add, sub, mul, div):
    global max_val, min_val
    
    if idx == N: # 연산횟수
        max_val = max(result, max_val)
        min_val = min(result, min_val)
        return
    
    if add:
        dfs(idx+1, result+arr[idx], add-1, sub, mul, div)
    if sub:
        dfs(idx+1, result-arr[idx], add, sub-1, mul, div)
    if mul:
        dfs(idx+1, result*arr[idx], add, sub, mul-1, div)
    if div:
        dfs(idx+1,\
            -(abs(result) // arr[idx]) if result < 0 else result // arr[idx],\
            add, sub, mul, div-1)

dfs(1, arr[0], add, sub, mul, div)
print(max_val)
print(min_val)