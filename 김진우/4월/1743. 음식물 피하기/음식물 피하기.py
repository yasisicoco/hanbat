from collections import deque

# N: 세로 길이, M: 가로 길이
N, M, K = map(int, input().split())
arr = [[0] * M for _ in range(N)]
for i in range(K):
    a, b = map(int, input().split())    
    arr[a-1][b-1] = 1 # 주어진 좌표값이 사람기준이다

# 1. 포문을 돌다가 1을 만나면 주면 상하좌우에 1을 카운팅하면서 움직임
# 2. 더 이상 주변에 1이 없다면 다시 처음 포문으로 돌아옴
# 3. 만약 한번 돌았던 1을 만나면 지나감 (쓰레기들은 연결되어있다)
# 4. 최대인 카운팅 숫자를 출력
def bfs(si, sj):
    global cnt
    
    di = [0, 1, -1, 0]
    dj = [1, 0, 0, -1]
    cnt += 1
    q = deque()
    q.append([si, sj])
    visited[i][j] = True
    
    while q:
        ci, cj = q.popleft()
        for k in range(4):
            ni = ci + di[k]
            nj = cj + dj[k]
            
            # 범위 안에 있고 / 안들렸던 곳이고 / 1이면 방문.
            if 0 <= ni < N and 0 <= nj < M and not visited[ni][nj] and arr[ni][nj] == 1:
                visited[ni][nj] = True
                cnt += 1
                q.append([ni, nj])
    
visited = [[False] * M for _ in range(N)]
result = 0
for i in range(N): # 세로
    for j in range(M): # 가로
        cnt = 0
        if arr[i][j] == 1: # 쓰레기 발견
            bfs(i, j)
            result = max(cnt, result) # 큰 쓰레기 갱신

print(result)