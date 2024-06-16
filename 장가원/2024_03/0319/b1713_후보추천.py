from sys import stdin; input = stdin.readline

N = int(input())    # 사진 틀의 수
rec_num = int(input())  # 추천 횟수
rec = list(map(int, input().split()))   # 추천 순서
pic = []
visit = [0] * N
for r in rec:
    # 빈 자리 있을 경우
    if len(pic) < N:
        # 이미 존재하는 경우
        if r in pic:
            visit[pic.index(r)] += 1
        # 없는 값
        else:
            pic.append(r)
            visit[len(pic) - 1] = 1
    # 빈 자리 없을 경우
    else:
        # 이미 존재
        if r in pic:
            visit[pic.index(r)] += 1
        # 없는 값
        else:
            # visit 값 가장 작은 거 삭제
            for p in range(len(pic)):
                if visit[p] == min(visit):
                    pic.remove(pic[p])
                    visit.pop(p)
                    visit.append(0)
                    break
            pic.append(r)
            visit[len(pic) - 1] = 1

pic.sort()
print(*pic)