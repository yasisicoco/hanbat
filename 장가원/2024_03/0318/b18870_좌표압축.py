# from sys import stdin; input = stdin.readline
# N = int(input())
# arr = list(map(int, input().split()))
# set_arr = list(set(arr))
# for num in arr:
#     cnt = 0
#     for snum in set_arr:
#         if snum < num:
#             cnt += 1
#     print(cnt, end=' ')

# from sys import stdin; input = stdin.readline
# N = int(input())
# arr = list(map(int, input().split()))
# set_arr = sorted(list(set(arr)))
# for num in arr:
#     print(set_arr.index(num), end=' ')

# from sys import stdin; input = stdin.readline
# N = int(input())
# arr = list(map(int, input().split()))
# set_arr = sorted(list(set(arr)))
# index_dic = {set_arr[i]:i for i in range(len(set_arr))}
# for num in arr:
#     print(index_dic[num], end=' ')

from sys import stdin; input = stdin.readline
N = int(input())
arr = list(map(int, input().split()))
set_arr = sorted(list(set(arr)))
index_dic = dict(zip(set_arr, list(range(len(set_arr)))))
for num in arr:
    print(index_dic[num], end=' ')

