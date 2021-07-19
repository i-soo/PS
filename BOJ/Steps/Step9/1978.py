n = int(input())
num_list = list(map(int, input().split()))

count = 0 # 소수 개수
for num in num_list :
    if num != 1 :	# 1은 소수가 아님
      for i in range(2, num) : # 2부터 자기자신을 제외한 수까지
        if num % i == 0 :   # 소수가 아닐 경우
	break
      else : 	# 소수인 경우
        count += 1
print(count)
