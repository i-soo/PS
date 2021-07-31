while True :
    nums = list(map(int, input().split()))
    if sum(nums) == 0:
        break  # 세 수가 0이면 break
        
    max_num = max(nums)  # 빗변
    nums.remove(max_num)  # 리스트에서 빗변 제거
    if nums[0]**2 + nums[1]**2 == max_num**2:  # 피타고라스 정리 만족 여부 판별
        print('right')
    else:
        print('wrong')
