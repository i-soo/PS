min_num = int(input())
max_num = int(input())
decimal_list = []   # 소수들을 담을 리스트
 
for i in range(min_num, max_num+1) :   # 첫 입력값과 두번째 입력값 사이에 대해 진행
    count = 0
    for j in range(1, i+1) :    # 1부터 i항까지
        if i % j == 0:
            count += 1
            if count > 2 :      # count 값이 2 이상인 경우 소수에 해당 안 됨
                break
    if count == 2 :             # 소수
        decimal_list.append(i)
if len(decimal_list) != 0 :     # 소수가 존재하는 경우
    print(sum(decimal_list))
    print(decimal_list[0])
else :                               
    print('-1')
