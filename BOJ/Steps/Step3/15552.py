import sys  # sys모듈 임포트

t= int(sys.stdin.readline()) #테스트 케이스 개수 t를 입력받음
# 여러 줄을 입력받는 것임을 고려해 input() 대신 sys모듈 이용해 시간 단축

for i in range(t):
    a,b = map(int, sys.stdin.readline().split())
    print(a+b)
