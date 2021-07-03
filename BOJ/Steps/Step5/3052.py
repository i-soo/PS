nums = []

for i in range(10):
    temp = int(input())
    nums.append(temp%42)

num_list = set(nums)
print(len(num_list))
