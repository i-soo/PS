# 한수 개수를 카운트하는 함수 정의
# 한수: 양의 정수이면서 각 자리가 등차수열을 이루는 경우
def count_hansu(n):
        cnt = 0
        if (n < 100):
            cnt = n
        else:
	    cnt = 99
            for i in range(100, n+1)
	         num_list = list(map(int, str(i)))

           	 if  num_list[0] - num_list[1] == num_list[1] - num_list[2] :
                    cnt += 1
        return cnt
 
inp = int(input())
result = count_hansu(inp)
print(result)
