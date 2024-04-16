N, K, T = map(int, input().split())
shark = list(map(int, input().split()))
shark.sort(reverse=True)

cnt = 0
st = []
feed = T
while cnt < K:
    
    if shark and shark[-1] < T: # 샤크에서 T보다 작은 애들을 꺼내서 순서대로저장
        st.append(shark.pop()) # 스택에 추가
    else:
        if st:
            feed = st.pop() # 꺼내서 저장
        else:
            print(T)
            exit()
       
        T += feed
        cnt += 1

print(T)