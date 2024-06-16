from sys import stdin; input = stdin.readline
N, M = map(int, input().split())
basic_score = list(map(int, input().split()))
get_scores = list(map(int, input().split()))
study_time = N * 24

score_time = []     # [시간당 점수, 시간]
for i in range(M):
    time = (100 - basic_score[i]) // get_scores[i]
    rem_score = (100 - basic_score[i]) % get_scores[i]
    # time 이라는 시간에, 한 시간 공부 당 얻는 점수
    score_time.append([get_scores[i], time])
    if rem_score:
        # 1시간에, 얻는 점수
        score_time.append([rem_score, 1])

score_time.sort(reverse=True)
sum_score = sum(basic_score)
# score : 시간당 점수, time : 시간
for score, time in score_time:
    if study_time > 0:
        sum_score += score * min(time, study_time)
        study_time -= min(time, study_time)
print(sum_score)