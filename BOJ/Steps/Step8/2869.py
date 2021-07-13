a, b, v = map(int, input().split())
# a= 올라가는 길이, b= 떨어지는길이, v= 나무높이 

result = (v-b)/(a-b)
print(int(result) if result == int(result) else int(result)+1)	#삼항연산자
