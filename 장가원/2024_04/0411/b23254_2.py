from sys import stdin; input = stdin.readline
# N x 24 : 공부 가능 시간, M : 시험 과목 수
N, M = map(int, input().split())
# 기본 점수
basic_scores = list(map(int, input().split()))
# 공부 1시간 당 올릴 수 있는 점수
get_scores = list(map(int, input().split()))
# 공부 가능 시간
study_time = N * 24

scores = []     # [get_scores, time] 집합
for i in range(M):
    time = (100 - basic_scores[i]) // get_scores[i]
    rem = (100 - basic_scores[i]) % get_scores[i]
    scores.append([get_scores[i], time])
    if rem != 0:
        scores.append([rem, 1])

scores.sort(reverse=True)
SUM = sum(basic_scores)       # 성적 합 구하기
for score, time in scores:
    SUM += score * min(time, study_time)
    study_time -= min(time, study_time)
print(SUM)
