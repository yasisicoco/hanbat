from sys import stdin; input = stdin.readline
k = int(input())
st = []
for _ in range(k):
    number = int(input())
    if number == 0:
        st.pop()
    else:
        st.append(number)
print(sum(st))
