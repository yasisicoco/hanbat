from sys import stdin; input = stdin.readline
N = int(input())

# -> 이 방향으로 바라봄
# 자기보다 낮은 빌딩만 볼 수 있음

cnt = 0
stack = []  # 오른쪽 빌딩 중 자신보다 작은 빌딩들
for _ in range(N):
    building = int(input())
    # building보다 큰 빌딩들은 stack에서 pop
    while stack and building >= stack[-1]:
        stack.pop()
    cnt += len(stack)   # building보다 작은 빌딩들 수의 합
    stack.append(building)
print(cnt)



'''
※ 풀이
생각의 전환이 필요한 문제이다. 내가 바라볼 수 있는 옥상 정원의 개수가 아니라 나를 바라보는 옥상의 개수를 구하는 것이다.

1. stack이 아니라 단순 스택이라고 불리는 내림차순, 올림차순을 유지하는 stack을 만드는 것이다.
2. 10, 3, 7, 4, 12, 2라고 했을 때 10은 일단 stack에 넣는다. [10] 10은 맨 왼쪽에 있기 때문에 바라볼 수 있는 옥상이 없다.
3. [10,3]은 3을 바라볼 수 있는 옥상 10이 있기에 len(stack) - 1(자기 자신을 바라볼 수 없으니)을 더해준다.
4. [10,7] 3을 pop하고 7이 들어간다. 이 과정을 끝까지 반복해주면 된다.
'''