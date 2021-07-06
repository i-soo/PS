# 풀이 a
n = input()
nums = input()

total = sum(map(int, nums))
print(total)

# 풀이 b 
n = input()
nums = input()

total = 0
for i in nums :     # 바로 요소에 접근
    total += int(i) 
print(total)

# 풀이 c
n = input()
nums = input()

total = 0
for i in range(n) :    # 인덱스로 요소에 접근
    total += int(nums[i])
print(total)
