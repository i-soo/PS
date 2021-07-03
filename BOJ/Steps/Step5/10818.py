# 풀이 a
n = int(input())
nums = list(map(int, input().split()))
print(min(nums), max(nums), sep=' ')

# 풀이 b
n = int(input())
nums = list(map(int, input().split()))
max = nums[0]
min = nums[0]

for i in nums[1:]:
    if i > max:
        max = i
    elif i < min:
        min = i

print(min, max, sep=' ')
