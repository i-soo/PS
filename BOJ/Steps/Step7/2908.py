# 풀이 a
num1, num2 = input().split()

n1_reversed = int(num1[::-1])  # [::-1] : 역순
n2_reversed = int(num2[::-1])

if n1_reversed > n2_reversed :
    print(n1_reversed)
else :
    print(n2_reversed)

    
# 풀이 b    
num1, num2 = map(str, input().split())

n1_reversed = ''.join(reversed(num1))
n2_reversed = ''.join(reversed(num2))

if n1_reversed > n2_reversed : 
	print(n1_reversed)
else : 
	print(n2_reversed)
