n = int(input())  # 배달해야 하는 설탕 kg 수

result = 0  # 봉지 수
while n >= 0:
    if n % 5 == 0:  # 5의 배수인 경우
        result += n // 5  # 5로 나눈 몫
        print(result)
        break
    n -= 3  # 설탕 kg 수가 5의 배수가 될 때까지 반복
    result += 1 # 봉지 추가
else:
    print(-1) # while 조건문이 거짓이 되면 -1 출력
