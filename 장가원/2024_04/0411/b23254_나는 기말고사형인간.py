from sys import stdin; input = stdin.readline
# N x 24 : 공부 가능 시간, M : 시험 과목 수
N, M = map(int, input().split())
# 기본 점수
basic_scores = list(map(int, input().split()))
# 공부 1시간 당 올릴 수 있는 점수
get_scores = list(map(int, input().split()))

# 한 과목 당 최대 100점
# 최종 성적 최댓값 구하기 (최종 성적은 모든 과목 성적 합)

# 공부 가능 시간
study_time = N * 24
scores = [(x, y, z) for x, y, z in zip([i for i in range(M)], basic_scores, get_scores)]
scores.sort(key=lambda x: x[2], reverse=True)

# ans = []
SUM = 0     # 성적 합
lack = []
for score in scores:
    temp = score[1]
    while temp <= 100 - score[2] and study_time > 0:
        temp += score[2]
        study_time -= 1
        if lack and study_time:
            if 100 - lack[0][1] > score[2]:
                # SUM += scores[lack[0][0]][2]
                SUM += 100 - lack[0][1]
                study_time -= 1
                lack.pop(0)
    if temp >= 100:
        temp = 100
    else:
        lack.append([score[0], temp])
    # ans.append(temp)
    SUM += temp

while lack and study_time > 0:
    SUM += 100 - lack[0][1]
    study_time -= 1
    lack.pop(0)

# print(study_time)
# print(ans)
# print(sum(ans))
print(SUM)
# 틀림
