from sys import stdin; input = stdin.readline

def boat():
    global cnt
    if boxes[0] > cranes[0]:
        return -1
    else:
        while boxes:
            for crane in cranes:
                for box in boxes:
                    if box <= crane:
                        boxes.remove(box)
                        break
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
