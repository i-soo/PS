t = int(input())  # 테스트 케이스 개수

for i in range(t):
    rep, s = input().split()
    rep = int(rep)
    s = str(s)
    
    for i in range(len(s)):
        print("{0}".format(s[i] * rep), end="")   # 포매팅
    print()
