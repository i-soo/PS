inp1 = int(input())  # int형으로 변환
inp2 = input()       # 문자열 그대로 저장

# 문자열의 인덱스를 이용
out1 = inp1 * int(inp2[2])
out2 = inp1 * int(inp2[1])
out3 = inp1 * int(inp2[0])
result = inp1 * int(inp2)

# sep='\n'로 한번에 출력 처리
print(out1, out2, out3, result, sep='\n')
