t = int(input()) # 테스트 케이스 개수

for i in range(t):
    h, w, n = map(int, input().split()) # h: 건물 층 수, w: 각 층의 방 수, n: 몇 번째 손님  
    num = n//h + 1 #방 번호
    floor = n % h
    if n % h == 0:  # h의 배수일 때
        num = n//h
        floor = h
    print(f'{floor * 100 + num}')
