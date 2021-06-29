inp1 = int(input())
inp2 = int(input()) # int형으로 변환
 
# 자릿수 각각을 계산
out1 = inp1*((inp2%100)%10)
out2 = inp1*((inp2%100)//10)
out3 = inp1*(inp2//100)
result = inp1*inp2

# sep='\n'로 한번에 출력 처리
print(out1, out2, out3, result, sep='\n')
