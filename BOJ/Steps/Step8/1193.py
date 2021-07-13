input = int(input())

line = 0  # 사선 라인
max = 0  # 입력받은 숫자의 라인에서 가장 큰 숫자
while input > max :
    line += 1  
    max += line  

gap = max - input
if line % 2 == 0 :  # 사선 라인이 짝수번째 일 때
    num_on_top = line - gap  #분자
    num_on_bottom = gap + 1  #분모
else :  # 사선 라인이 홀수번째 일 때
    num_on_top = gap + 1  
    num_on_bottom = line - gap  
print(f'{num_on_top}/{num_on_bottom}')
