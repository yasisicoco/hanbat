def select(num):
    if num == N + 1:
        return
    if num > 0:
        if visited[num] == 0:
            visited[num] = 1
            subset.append((num, numbers[num]))
            return select(num + 1)
    return select(num + 1)


N = int(input())
numbers = [0]
for _ in range(N):
    numbers.append(int(input()))
subset = []
visited = [0] * (N + 1)
# for num in range(N + 1):
#     subset.append((num, numbers[num]))

select(0)

print(numbers)
print(subset)