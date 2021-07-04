n = int(input())  # 테스트 케이스 개수 입력

 for i in range(n):
    a = input()   # OX퀴즈 결과
    b = list(a)  # 결과를 리스트로
    
    cnt = 0   # 'O' 개수
    sum = 0   # 총합
    for l in b:
      if l == 'X':
         cnt = 0   # 'X' 다음에 오는 'O'는 다시 0점부터
      else:
         cnt += 1
         sum += cnt  # 값을 구하는 즉시 더해줌
    print(sum)
