h, m = map(int, input().split())

if m >= 45 :	# 처음 설정해 놓은 분단위가 45분보다 클 때 
        print(h, m-45)
elif m<45 and h>0 :	# 0분에서 45분 사이의 값일 때
        print(h-1, m+15)
else :	            # h=0일 때 
        print(23, m+15)
