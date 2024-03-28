N = int(input())
arr = list(map(int, input().split()))
stack1 = []  # 한 명씩 설 수 있는 공간
stack2 = [0]  # 간식 받는 곳

ans = 'Nice'
for i in range(N):
    if not stack1:
        if arr[i] != stack2[-1]+1:  # 맨 처음 학생의 번호가 1이 아니라면 대기공간으로
            stack1.append(arr[i])
            continue
        elif arr[i] == stack2[-1]+1:  # 처음 학생의 번호가 1이라면 간식 받는 곳으로
            stack2.append(arr[i])
            continue




    if stack1[-1] >= arr[i]:  # 한 명씩 설 수 있는 공간의 학생번호가 크다면
        if stack2:
            if stack2[-1] + 1 == arr[i]:  # 간식 받은 사람보다 줄서있는 학생번호의 수가 1 크다면
                stack2.append(arr[i])
            else:   # 줄 서있는 학생번호가 2이상이면 대기공간으로
                stack1.append(arr[i])
        else:  # 간식받은 사람이 없으면
            if arr[i] == 1:
                stack2.append(arr[i])

            else:
                stack1.append(arr[i])

    if stack1[-1] < arr[i]:  # 한 명씩 설 수 있는 공간보다 현재 서있는 곳의 학생번호가 크다면
        ans = 'Sad'
        break

    while stack2 and stack1 and stack2[-1] + 1 == stack1[-1]:
        x = stack1.pop()
        stack2.append(x)

print(ans)
