a, b, c = map(int, input().split())

# sep='\n'로 한번에 출력 처리
print((a+b)%c, ((a%c)+(b%c))%c, (a*b)%c, ((a%c)*(b%c))%c, sep='\n')
