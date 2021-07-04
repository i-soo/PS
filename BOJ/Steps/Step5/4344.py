C = int(input())

for i in range(C):
    inp = list(map(int, input().split(' ')))
    
    cnt =0    # 평균 이상인 점수 개수
    if inp[0] == len(inp)-1:
       avg = (sum(inp)-inp[0]) / inp[0]
    
    for j in range(1, len(inp)):
        if inp[j] > avg :
           cnt +=1
            
    print('%.3f%%'%((cnt/inp[0])*100))   # 소수점 아래 3번째까지
