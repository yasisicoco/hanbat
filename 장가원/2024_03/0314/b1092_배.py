from sys import stdin; input = stdin.readline

def boat():
    global cnt
    if boxes[0] > cranes[0]:
        return -1
    else:
        while boxes:
            for i in range(N):
                if not boxes:
                    if i != 0:
                        cnt += 1
                    break
                if cranes[i] >= boxes[0]:
                    boxes.remove(boxes[0])
            else:
                cnt += 1
        return cnt

# N : 크레인 수
N = int(input())    # 50 이하
# 각 크레인의 무게 제한
cranes = list(map(int, input().split()))
cranes.sort(reverse=True)
# M : 박스 수
M = int(input())    # 10,000 이하
# 각 박스의 무게
boxes = list(map(int, input().split()))
boxes.sort(reverse=True)

cnt = 0
print(boat())



'''
3
9 8 6
5
7 5 4 2 2 

'''